# Datasets for Apical-in & Apical-out Classification

## Data Source
The dataset consists of microscopic images of neuroepithelial organoids expressing ZO1-EGFP. These images are used to classify cell configurations as **Apical-in** or **Apical-out** based on intensity distribution and spatial properties.

### Data Description
- **File Format**: `.tif` (Tagged Image File Format)
- **Channels**: Single-channel grayscale images
- **Resolution**: Varies per dataset
- **Dataset Size**: Images are analyzed individually, with cell segmentation and classification performed for each image.

## Data Validation
To ensure the dataset meets the project requirements, the following validation steps were performed:
1. **Intensity Normalization**: Image pixel values were scaled between 0 and 1.
2. **Thresholding (Otsu’s Method)**: Used to segment cells based on grayscale intensity.
3. **Minimum Cell Area Filtering**: Objects with areas below 100 pixels were removed.
4. **Distance Transform Analysis**: Used to classify cells based on high-intensity pixel distribution.

## Data Availability
The dataset is currently stored locally and can be accessed from:
- **Path**: `/Users/fenggeshan/Desktop/WIP006_G10C.tif`
- **Dataset Repository**: `[Insert dataset repository URL if applicable]`

## Expected Outputs
Each processed image generates:
1. **Cell classification data (CSV)**:
   - Total cell area, apical area, non-apical area, and classification results.
2. **Annotated overlay image (PNG)**:
   - Cells classified as **Apical-in** (red) and **Apical-out** (blue).

## Dataset Link
[Insert dataset download URL or repository link]
