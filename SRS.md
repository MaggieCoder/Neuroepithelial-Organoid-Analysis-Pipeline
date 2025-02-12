# Software Requirements Specification (SRS)

## 1. Introduction
### 1.1 Purpose
This project aims to classify **Apical-in** and **Apical-out** cell configurations in neuroepithelial organoid images based on ZO1-EGFP intensity and spatial distribution. The tool processes grayscale `.tif` images and outputs classification results in CSV format along with annotated images.

### 1.2 Scope
The software performs the following tasks:
- Load `.tif` images and convert them to grayscale if needed.
- Perform **Otsu thresholding** for initial segmentation.
- Identify individual cells and compute their spatial properties.
- Classify cells based on **high-intensity distance ratio**.
- Generate output files for analysis and visualization.

### 1.3 Intended Audience
- Researchers studying neuroepithelial organoid development.
- Computational biologists working with image-based cell analysis.
- Bioinformatics students and professionals analyzing microscopic images.

### 1.4 Definitions and Acronyms
- **ZO1-EGFP**: A fluorescent marker highlighting tight junctions in epithelial cells.
- **Apical-in**: Cells with high-intensity regions concentrated towards the center.
- **Apical-out**: Cells with high-intensity regions near the periphery.
- **Otsu’s Method**: A technique for automatic threshold selection in image segmentation.

---

## 2. Functional Requirements
### 2.1 Data Input
- Accepts **single-channel grayscale images** in `.tif` format.
- Supports local file loading (`image_path` parameter in code).
- Processes images of varying sizes and resolutions.

### 2.2 Image Processing
- Convert multi-channel images to grayscale.
- Apply Otsu’s thresholding for segmentation.
- Remove small objects (min cell area: 100 pixels).
- Perform **morphological operations** for noise reduction.

### 2.3 Cell Classification
- Compute **Euclidean distance transform** for each segmented cell.
- Identify **high-intensity pixels** based on a fraction (default: 0.8) of the max intensity.
- Calculate **mean high-intensity distance ratio**.
- Classify cells based on a threshold ratio (default: 0.5).

### 2.4 Output Generation
- **CSV File**:
  - Cell area, apical area, non-apical area, percentage of apical area, classification.
- **Annotated Image (PNG)**:
  - **Blue cells** → Apical-out  
  - **Red cells** → Apical-in

---

## 3. Non-Functional Requirements
### 3.1 Performance
- Must process a single image in **under 30 seconds** on a standard research workstation.

### 3.2 Usability
- Code should be modular and well-documented for ease of modification.
- Outputs should be human-readable and easily interpretable.

### 3.3 Scalability
- The tool should handle multiple images in batch mode for larger datasets.
- Should support different intensity thresholds for different imaging conditions.

---

## 4. References
- [Skimage Library Documentation](https://scikit-image.org/)
- [SciPy ndimage Documentation](https://docs.scipy.org/doc/scipy/reference/ndimage.html)
- [Matplotlib for Image Visualization](https://matplotlib.org/)
