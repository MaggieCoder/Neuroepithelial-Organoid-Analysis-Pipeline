---
"GitHub WBS: Apical-in & Apical-out Image Analysis Pipeline"
---

# **GitHub WBS: Apical-in & Apical-out Image Analysis Pipeline**
## **1. Repository Setup**
- [ ] Create a GitHub repository (e.g., `Apical_Analysis`)
- [ ] Add a `README.md` file with project description
- [ ] Create a `.gitignore` file (ignore `.csv`, `.png`, temporary files)
- [ ] Set up folder structure:
  - `src/` (for scripts)
  - `data/` (for sample images)
  - `results/` (for output CSV and images)
  - `docs/` (for documentation)
- [ ] Add an MIT or BSD license
---

## **2. Core Functionality Implementation**
### **2.1 Image Preprocessing**
- [ ] Load `.tif` image using `skimage.io`
- [ ] Convert to grayscale if necessary
- [ ] Normalize pixel intensity
- [ ] (Optional) Invert image if needed

### **2.2 Segmentation & Cell Detection**
- [ ] Apply Otsu thresholding for binary segmentation
- [ ] Fill holes in cell masks
- [ ] Remove small objects based on `min_cell_area`
- [ ] Perform morphological closing for better segmentation

### **2.3 Cell Feature Extraction**
- [ ] Label individual cells
- [ ] Extract properties using `skimage.measure.regionprops`
- [ ] Compute Euclidean distance transform for each cell
- [ ] Identify high-intensity regions based on threshold
- [ ] Calculate high-intensity distance ratio

### **2.4 Apical-in & Apical-out Classification**
- [ ] Compute total, apical, and non-apical areas
- [ ] Determine apical percentage
- [ ] Classify cells based on `distance_ratio_threshold`
- [ ] Assign color overlays (blue = Apical-out, red = Apical-in)

### **2.5 Result Output**
- [ ] Store results in a Pandas DataFrame
- [ ] Save classification results as a CSV file
- [ ] Generate an overlay image with colored classification
- [ ] Save and display overlay visualization
---

## **3. Testing & Debugging**
- [ ] Add test images to `data/`
- [ ] Implement unit tests for preprocessing, segmentation, and classification
- [ ] Validate classification accuracy on known datasets
- [ ] Debug errors in cell detection and classification
---

## **4. Documentation & User Guide**
- [ ] Write a `README.md` with:
  - Project overview
  - Installation guide
  - Usage instructions
  - Example results
- [ ] Add inline code comments for better readability
- [ ] Provide sample images in `data/` folder
- [ ] Create a troubleshooting guide for common issues
---

## **5. GitHub Automation & Finalization**
- [ ] Write a `requirements.txt` or `environment.yml` for dependencies
- [ ] Set up GitHub Actions for automated testing (if needed)
- [ ] Release first stable version (`v1.0`)
- [ ] Share repository link with collaborators or publish
---
