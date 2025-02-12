---
```markdown
# Datasets for Apical-in & Apical-out Classification

## Data Source
The dataset consists of microscopic images of neuroepithelial organoids expressing ZO1-EGFP. These images are used to classify cell configurations as **Apical-in** or **Apical-out** based on intensity distribution and spatial properties.

### Data Description
- **File Format**: `.tif` (Tagged Image File Format)
- **Channels**: Single-channel grayscale images
- **Resolution**: Typically 512×512 to 2048×2048 pixels.
- **Dataset Size**: Images are analyzed individually, with cell segmentation and classification performed for each image.

## Data Validation
To ensure the dataset meets the project requirements, the following validation steps were performed:
1. **Intensity Normalization**: Image pixel values were scaled between 0 and 1.
2. **Thresholding (Otsu’s Method)**: Used to segment cells based on grayscale intensity.
3. **Minimum Cell Area Filtering**: Objects with areas below 100 pixels were removed.
4. **Distance Transform Analysis**: Used to classify cells based on high-intensity pixel distribution.

## Data Availability
- **Storage**: Hosted in a secure repository.
- **Dataset Repository**: [GitHub Repository](https://github.com/your-repo/dataset) (or alternative storage)
- **Access**: Available upon request.

## Expected Outputs
Each processed image generates:
1. **Cell classification data (CSV)**:
   - **Format**:
     | Image ID  | Total Cell Area | Apical Area | Non-Apical Area | Classification |
     |-----------|----------------|-------------|-----------------|----------------|
     | img001.tif | 2000 px²       | 1200 px²    | 800 px²         | Apical-in      |
     | img002.tif | 2500 px²       | 500 px²     | 2000 px²        | Apical-out     |

2. **Annotated overlay image (PNG)**:
   - **Red**: Apical-in cells
   - **Blue**: Apical-out cells

## Dataset Link
[Dataset Repository](https://github.com/your-repo/dataset)

## Data Loading Example
```python
import cv2
import numpy as np

# Load image
image = cv2.imread("WIP006_G10C.tif", cv2.IMREAD_GRAYSCALE)

# Normalize intensity
image = image / 255.0

# Apply Otsu thresholding
_, binary = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Display processed image
cv2.imshow("Segmented Cells", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
