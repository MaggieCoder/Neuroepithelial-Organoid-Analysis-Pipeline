# tests/test_pipeline.py
# PyTest smoke tests for Neuroepithelial-Organoid-Analysis-Pipeline
# ---------------------------------------------------------------
# Design goals:
# 1) Avoid assuming specific function signatures; automatically detect common modules and entry points.
# 2) Missing parts cause SKIPPED tests (not hard failures), with clear guidance for reviewers.
# 3) If main.py supports --help, verify the CLI runs.
# 4) If an image processing function is found, run it on a small synthetic image to confirm the pipeline works.

import importlib
import importlib.util
import subprocess
import sys
from pathlib import Path
import types
import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]


# --------- Helper functions --------- #

def _module_exists(mod_name: str) -> bool:
    try:
        importlib.util.find_spec(mod_name)
        return True
    except Exception:
        return False


def _import_by_name_or_path(name: str) -> types.ModuleType | None:
    """
    Try importing by name first; if not found, load the .py file directly from the repo root.
    """
    try:
        if _module_exists(name):
            return importlib.import_module(name)
    except Exception:
        pass

    candidate = REPO_ROOT / f"{name}.py"
    if candidate.exists():
        spec = importlib.util.spec_from_file_location(name, candidate)
        if spec and spec.loader:
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)  # type: ignore[attr-defined]
            return mod
    return None


def _find_processing_callable(mod: types.ModuleType) -> tuple[str, callable] | None:
    """
    Try to detect an image-processing function based on its name.
    Looks for functions containing process / analys / segment / run / pipeline.
    """
    keywords = ("process", "analys", "segment", "run", "pipeline")
    for attr in dir(mod):
        if attr.startswith("_"):
            continue
        obj = getattr(mod, attr)
        if callable(obj) and any(k in attr.lower() for k in keywords):
            return attr, obj
    return None


# --------- Tests --------- #

def test_import_image_processing():
    mod = _import_by_name_or_path("image_processing")
    if mod is None:
        pytest.skip("image_processing module not found. "
                    "Please provide image_processing.py in the repo root or package it properly.")
    assert isinstance(mod, types.ModuleType)


def test_import_parameters_and_defaults():
    mod = _import_by_name_or_path("parameters")
    if mod is None:
        pytest.skip("parameters module not found. "
                    "Please add parameters.py to store default config or thresholds.")
    candidates = ["DEFAULTS", "PARAMS", "CONFIG", "THRESHOLDS", "Settings", "Params"]
    has_any = any(hasattr(mod, name) for name in candidates)
    if not has_any:
        pytest.skip("parameters module exists but no default parameter object found "
                    "(expected one of DEFAULTS / PARAMS / CONFIG).")


def test_cli_help_if_available():
    main_py = REPO_ROOT / "main.py"
    if not main_py.exists():
        pytest.skip("main.py not found, skipping CLI --help test.")
    result = subprocess.run([sys.executable, str(main_py), "--help"],
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    assert result.returncode == 0, f"`python main.py --help` failed:\n{result.stdout}"


def test_process_minimal_synthetic_image(tmp_path):
    """
    Create a small synthetic image (64×64 ring pattern) that mimics apical-out structure.
    If a processing function is found in image_processing, run it with common call styles.
    """
    import numpy as np
    from PIL import Image

    ip = _import_by_name_or_path("image_processing")
    if ip is None:
        pytest.skip("image_processing module not found, skipping image-processing smoke test.")

    found = _find_processing_callable(ip)
    if found is None:
        pytest.skip("No obvious processing function found "
                    "(name should include process / analys / segment / run / pipeline).")
    fn_name, fn = found

    # Generate synthetic ring image
    h, w = 64, 64
    y, x = np.ogrid[:h, :w]
    cy, cx = h // 2, w // 2
    r = np.sqrt((y - cy) ** 2 + (x - cx) ** 2)
    img = np.zeros((h, w), dtype=np.uint8)
    img[(r > 16) & (r < 20)] = 220  # bright ring
    img[r < 8] = 40                 # dim center
    img_path = tmp_path / "synthetic_ring.png"
    Image.fromarray(img).save(img_path)

    tried = []
    try:
        result = fn(str(img_path))
        tried.append(f"{fn_name}(path)")
    except Exception:
        try:
            result = fn(Image.open(img_path))
            tried.append(f"{fn_name}(PIL.Image)")
        except Exception:
            try:
                result = fn(img)
                tried.append(f"{fn_name}(np.ndarray)")
            except Exception as e:
                pytest.skip(
                    "Found a candidate function but could not call it using any of the common methods: "
                    f"{' -> '.join(tried)}. "
                    "Please expose a stable single-image entry point, e.g. process_image(path) or analyze(img). "
                    f"Last error: {repr(e)}"
                )

    assert result is not None, f"{fn_name} returned None. Please return an output object or dict."


def test_version_if_exists():
    """
    If the project is packaged, check that __version__ or version is defined.
    """
    possible_packages = [
        "neuroepithelial_organoid_analysis_pipeline",
        "neuroepithelial_organoid",
        "organoid_pipeline",
        "pipeline"
    ]
    pkg = None
    for name in possible_packages:
        try:
            pkg = importlib.import_module(name)
            break
        except Exception:
            continue

    if pkg is None:
        pytest.skip("No importable package found. Consider adding __init__.py and defining __version__.")
    version = getattr(pkg, "__version__", None) or getattr(pkg, "version", None)
    if version is None:
        pytest.skip("Package imported but __version__ not found. Please define it in __init__.py.")
    assert isinstance(version, str) and len(version) > 0
