# **Software Requirements Specification (SRS)**

## **1. Introduction**

### **1.1 Purpose**
This project aims to classify **Apical-in** and **Apical-out** cell configurations in neuroepithelial organoid images based on **ZO1-EGFP intensity and spatial distribution**. The tool processes grayscale `.tif` images and outputs classification results in **CSV format** along with **annotated images**.

### **1.2 Scope**
The software performs the following tasks:
- Load `.tif` images and convert them to grayscale if needed.
- Perform **Otsu thresholding** for initial segmentation.
- Identify individual cells and compute their spatial properties.
- Classify cells based on **high-intensity distance ratio**.
- Generate output files for analysis and visualization.

### **1.3 Intended Audience**
- Researchers studying **neuroepithelial organoid development**.
- Computational biologists working with **image-based cell analysis**.
- Bioinformatics students and professionals analyzing **microscopic images**.

### **1.4 Definitions and Acronyms**
- **ZO1-EGFP**: A fluorescent marker highlighting **tight junctions** in epithelial cells.
- **Apical-in**: Cells with **high-intensity regions concentrated towards the center**.
- **Apical-out**: Cells with **high-intensity regions near the periphery**.
- **Otsu’s Method**: A technique for **automatic threshold selection** in image segmentation.
- **High-intensity distance ratio**: The ratio of **high-intensity pixel distribution** in a segmented cell.

### **1.5 System Overview**
The system processes **grayscale microscopic images** and classifies neuroepithelial organoid cells as **Apical-in** or **Apical-out**. The processing workflow is as follows:

1. **Load Image**: The system loads `.tif` grayscale images.
2. **Preprocessing**: Converts multi-channel images to grayscale (if needed) and applies **Otsu’s thresholding** for segmentation.
3. **Feature Extraction**: Computes cell spatial properties and high-intensity pixel distribution.
4. **Classification**: Uses a **threshold-based approach** to classify cells.
5. **Output Generation**: Produces **CSV reports** and **annotated images** with visualized classifications.

---

## **2. Functional Requirements**

### **2.1 Data Input**
- Accepts **single-channel grayscale images** in `.tif` format.
- Supports **batch processing** for multiple images (file list input or directory scanning).
- Input images should follow the **naming convention**: `sample_001.tif`, `sample_002.tif`, etc.
- Processes images of varying **sizes and resolutions**.

### **2.2 Image Processing**
- Convert **multi-channel images** to grayscale if necessary.
- Apply **Otsu’s thresholding** to segment the image.
- Remove **small objects** (minimum cell area: 100 pixels).
- Perform **morphological operations** for noise reduction.

### **2.3 Cell Classification**
- Compute **Euclidean distance transform** for each segmented cell.
- Identify **high-intensity pixels** based on a fraction (default: **0.8**) of the max intensity.
- Calculate the **mean high-intensity distance ratio**.
- Classify cells based on a **threshold ratio** (default: **0.5**).
- If **multiple high-intensity clusters** are present, use **majority voting** to determine classification.

### **2.4 Output Generation**
- **CSV File** (Classification results):
  - **Columns**: `Image ID`, `Total Cell Area`, `Apical Area`, `Non-Apical Area`, `% Apical Area`, `Classification`
  - Example:
    | Image ID   | Total Cell Area | Apical Area | Non-Apical Area | % Apical Area | Classification |
    |------------|----------------|-------------|-----------------|---------------|----------------|
    | sample_001 | 2000 px²       | 1200 px²    | 800 px²         | 60%           | Apical-in      |
    | sample_002 | 2500 px²       | 500 px²     | 2000 px²        | 20%           | Apical-out     |

- **Annotated Image (PNG)**:
  - **Blue cells** → Apical-out  
  - **Red cells** → Apical-in  

### **2.5 Error Handling**
- **Invalid Input Format**: If the image format is incorrect (not `.tif`), the program raises an error.
- **Corrupt or Missing Data**: If the input image is unreadable, the tool logs an error and continues processing other images.
- **Empty Segmentation Output**: If no cells are detected after thresholding, the system outputs a warning but does not crash.
- **Incorrect Parameter Values**: The system ensures parameters (e.g., intensity threshold) are within an acceptable range.

---

## **3. Non-Functional Requirements**

### **3.1 Performance**
- The tool should process a **1024×1024 resolution** image within **≤ 30 seconds**.
- Expected hardware: **Intel i7 (or equivalent) processor, 16GB RAM, SSD storage**.
- Benchmarks:
  - **512×512 image**: ~5 seconds
  - **1024×1024 image**: ~20 seconds
  - **2048×2048 image**: ~45 seconds (not recommended)

### **3.2 Usability**
- The code should be **modular and well-documented** for ease of modification.
- Outputs should be **human-readable** and easily interpretable.

### **3.3 Scalability**
- The tool should support **batch processing** for large datasets.
- Should allow **custom intensity thresholds** for different imaging conditions.

---

## **4. References**
- [Skimage Library Documentation](https://scikit-image.org/)
- [SciPy ndimage Documentation](https://docs.scipy.org/doc/scipy/reference/ndimage.html)
- [Matplotlib for Image Visualization](https://matplotlib.org/)

---

## **5. Future Extensions**
- **Deep Learning Model Integration**: Implement a CNN-based classifier for improved accuracy.
- **Web Interface**: Develop a web-based tool for real-time image analysis.
- **3D Image Support**: Extend classification to **3D organoid reconstructions**.

---
