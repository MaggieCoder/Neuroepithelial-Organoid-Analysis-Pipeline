# Neuroepithelial-Organoid-Analysis-Pipeline

Overview
This project provides a robust image analysis pipeline to quantitatively distinguish between apical-out and apical-in configurations in neuroepithelial organoids based on fluorescence imaging of ZO1-EGFP or other tight junction markers.

Features
- Radial Intensity Analysis: Classifies ZO1-EGFP regions as apical-out or apical-in based on their radial distribution.
- Quantification: Calculates the percentage of cells with apical-out and apical-in configurations.
- Batch Processing: Supports analyzing multiple images in a single run.
- Visualization:
  - Annotated images with color-coded regions (apical-out vs. apical-in).
  - Graphs showing radial intensity distributions.
  - Summary statistics exported as CSV.
- Extensibility: Supports customization for other tight junction markers or configurations.

---

### **1. Programming Environment** 🖥️
- **Python**: Flexible and widely used for image analysis.
  - Install Python: [Download Python](https://www.python.org/downloads/) 🐍
- **Optional**: MATLAB, if preferred for image processing.

---

### **2. Python Libraries** 📚
#### **Core Libraries** 🔧
- `numpy`: For numerical computations.
  ```bash
  pip install numpy
  ```
- `pandas`: For managing and analyzing tabular data.
  ```bash
  pip install pandas
  ```

#### **Image Processing** 🖼️
- `scikit-image`: For advanced image processing (segmentation, feature extraction).
  ```bash
  pip install scikit-image
  ```
- `opencv-python`: For general image handling and processing.
  ```bash
  pip install opencv-python
  ```
- `Pillow`: For basic image handling.
  ```bash
  pip install pillow
  ```

#### **Visualization** 📊
- `matplotlib`: For plotting and visualizing data.
  ```bash
  pip install matplotlib
  ```
- `seaborn`: For enhanced data visualization.
  ```bash
  pip install seaborn
  ```

#### **Scientific Computation** 🔬
- `scipy`: For spatial analysis and advanced computations.
  ```bash
  pip install scipy
  ```

#### **Machine Learning/Feature Analysis** 🤖
- `scikit-learn`: For clustering and classification tasks, if needed.
  ```bash
  pip install scikit-learn
  ```

#### **Deep Learning (if needed)** 🧠
- `tensorflow` or `pytorch`: For training models to classify apical-out vs. apical-in regions.
  ```bash
  pip install tensorflow
  # OR
  pip install torch torchvision
  ```

#### **3D Visualization** 🔍
- `napari`: For interactive 3D image visualization.
  ```bash
  pip install napari[all]
  ```

---

### **3. Additional Tools** 🛠️
#### **For Image Annotation** 📝
- **Fiji/ImageJ** (with bio-formats plugin): A versatile image analysis tool for manual annotations and preprocessing.
  - Download: [Fiji](https://imagej.net/software/fiji/)

#### **For Data Management** 🗃️
- **QuPath**: A powerful open-source tool for whole-slide image analysis. Can also be used for Z-stack images.
  - Download: [QuPath](https://qupath.github.io/)

---

### **4. Hardware Requirements** 💻
- Ensure your system has sufficient GPU support (if using deep learning libraries like TensorFlow or PyTorch) for faster processing.

### **Installation Environment** 🚀
- Use a virtual environment like `venv` or `conda` to isolate dependencies.
  ```bash
  python -m venv env
  source env/bin/activate  # For Linux/macOS
  .\env\Scripts\activate   # For Windows
  ```

---

### **1. Biological Question** 🧬
The project aims to answer:
- What is the spatial configuration of neuroepithelial organoids based on apical polarity?
- Specifically, what proportion of cells exhibit apical-out vs. apical-in configurations, as defined by the localization of ZO1-EGFP, a tight junction marker?
- How does the apical configuration vary under different experimental conditions? For example, conditions such as extracellular matrix (ECM) composition, growth factors, or genetic manipulations.

This analysis will provide insights into the structural organization and polarity of organoids, contributing to our understanding of tissue architecture and its role in organoid function and development.

---

### **3. Input and Output Data** 📥📤
#### **Input Data** 📁
- **Image Data**:
  - Format: Multichannel Z-stack images (e.g., .tif, .czi, .nd2).
  - Dimensions: 3D (x, y, z) with an additional channel for fluorescence.
  - Content:
    - Channel 1: ZO1-EGFP fluorescence signal.
    - Optional Channel: Nuclear counterstain (e.g., DAPI) for cell counting.
  - Source: Confocal or widefield microscopy.
- **Metadata**:
  - Image acquisition settings (e.g., voxel size, magnification, laser intensity).
  - Experimental condition identifiers (e.g., sample ID, treatment, or genetic condition).

#### **Output Data** 📊
- **Quantitative Data**:
  - Proportions:
    - Percent of cells with apical-out vs. apical-in configurations.
    - Number of cells with apical signal for each configuration.
  - Measurements:
    - ZO1 signal intensity for apical-out vs. apical-in regions.
    - Total signal distribution across Z-stack slices.
  - Format: .csv or .xlsx file.
- **Visualizations**:
  - Images:
    - Processed images with segmented regions marked as apical-out or apical-in.
    - Highlighted ZO1 signal in 3D projections or 2D slices. Format: .png or .tif.
  - Plots:
    - Bar plots of apical-out vs. apical-in percentages.
    - Heatmaps of ZO1 signal intensity.
- **Report**:
  - A summary of the analysis, including key statistics and visualizations.
  - Format: .pdf or .html.

---

### **Pipeline Workflow Overview** 🔄
#### **Preprocessing**:
- Load Z-stack image data.
- Denoise and normalize fluorescence intensity.

#### **Segmentation**:
- Identify regions of interest (ROIs) using ZO1 signal.
- Classify ROIs as apical-out or apical-in based on location.

#### **Quantification**:
- Calculate proportions of apical-out and apical-in configurations.
- Measure signal intensity and distribution.

#### **Visualization & Reporting**:
- Generate labeled images, plots, and a summary report.

---
