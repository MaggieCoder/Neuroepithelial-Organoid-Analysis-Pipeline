# Dataset Documentation
mentation

Real dataset for answering a biological question using the tool

The selected real dataset comprises fluorescence microscopy images of neuroepithelial organoids expressing ZO1-EGFP, a tight junction marker crucial for identifying apical membrane regions. The dataset includes approximately 120 images captured using confocal microscopy, with each image representing individual organoids. Images have dimensions of approximately 1024 × 1024 pixels, are in TIFF format, and display varying configurations of apical polarity—specifically "apical-in" and "apical-out" phenotypes. Basic statistics indicate that approximately 60% of organoids demonstrate an "apical-in" orientation, while around 40% exhibit "apical-out" polarity under standard conditions.

Justification:
This dataset is ideal for the developed image analysis pipeline because it contains clearly distinguishable morphologies for automated segmentation and classification. The ZO1-EGFP marker provides high-contrast labeling of cell boundaries, facilitating precise delineation and robust quantitative analyses using the developed pipeline.

Biological Question:
Does exposure of neuroepithelial organoids to lysophosphatidic acid (LPA) reliably induce a shift from apical-in to apical-out polarization?

Expected Results:
The pipeline is expected to quantitatively confirm an increase in "apical-out" organoid configurations upon LPA treatment compared to control conditions. Specifically, images treated with LPA are anticipated to show a significant increase in the percentage of organoids classified as "apical-out," supported by increased intensity and altered distribution patterns of ZO1-EGFP fluorescence along the organoid surface.

Expected Answer:
Exposure to LPA significantly enhances the incidence of "apical-out" orientation in neuroepithelial organoids, validating LPA as a potent regulator of epithelial cell polarity via the GPCR/Rho/ROCK/F-actin signaling pathway.

## Example dataset for using the tool
We provide an example dataset consisting of four `.tif` microscopy images located in the `data/` folder of this repository. These images are labeled as:

    "Sample_A.tif",
    "Sample_B.tif",
    "Sample_C.tif",
    "Sample_D.tif",

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
