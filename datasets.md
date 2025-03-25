# Dataset Documentation

## Example dataset for using the tool

We provide an example dataset consisting of four `.tif` microscopy images located in the `data/` folder of this repository. These images are labeled as:

- `WIP006_G12A.tif`
- `WIP006_G12B.tif`
- `WIP006_G12C.tif`
- `WIP006_G12D.tif`

Each image has a resolution of approximately 1000 × 1000 pixels and is either grayscale or RGB depending on acquisition. The total size of the dataset is around 5.2 MB, making it lightweight enough to be included in the repository (well under the 20MB threshold).

This dataset was collected from neuroepithelial organoids during apical polarity screening experiments. It contains representative variations in morphology, including cells with outward-facing apical surfaces (“apical-out” cells). The images are ideal for testing the pipeline's segmentation, filtering, and classification capabilities under various parameter settings.

### Data folder location

The data files can be found in the following directory:https://github.com/MaggieCoder/Neuroepithelial-Organoid-Analysis-Pipeline/tree/main/image


### Why this dataset is a good example

- It is representative of real-world use cases where detecting apical-out polarity is relevant for organoid morphology research.
- It includes cells of varying shapes, intensities, and areas, allowing for effective demonstration of thresholding and morphological filtering.
- It is small and fast to process, which makes it convenient for testing and debugging during development.
- The data leads to clearly interpretable visual results and meaningful summary statistics.

### Packaging and distribution compliance

This project follows standard Python packaging practices for including data files. The dataset is stored in a local `data/` folder and referenced through `parameters.py` in a dictionary structure called `image_files`, ensuring dynamic loading without hardcoding absolute paths.

To comply with Python packaging guidelines, we refer to the official setuptools documentation for including data files in a package:

📦 https://setuptools.pypa.io/en/latest/userguide/datafiles.html

If this package is to be distributed as a pip-installable module, we would include appropriate entries in `MANIFEST.in` and configure `setup.py` to ensure the `data/` directory is included with the package.
