<h1 align="center">
  🎀 Neuroepithelial-Organoid-Analysis-Pipeline 🎀<br>
  <sub>A Bioinformatics Project for Image Analysis</sub>
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-pink" alt="Python Version">
  <img src="https://img.shields.io/badge/Status-Active-pink" alt="Project Status">
  <img src="https://img.shields.io/badge/License-MIT-pink" alt="License">
</p>

---

## 🌸 Overview

This bioinformatics pipeline is designed to analyze **neuroepithelial organoids** and classify cells as **Apical-in** or **Apical-out** based on ZO1-EGFP fluorescence intensity. The goal is to generate **quantitative data** for a manuscript currently under revision. 🧫✨

By studying **apical membrane formation** and **epithelial cell polarity**, we can gain insights into the mechanisms that regulate neuroepithelial development! 🧠🔬

---

## 🎯 Research Goal

🧬 **Biological Question:**
> How do apical membrane formation and epithelial polarity emerge in neuroepithelial organoids?

📜 **Project Description:**
This project develops an image analysis pipeline that quantitatively classifies neuroepithelial organoid cells into **Apical-in** or **Apical-out** categories based on fluorescence intensity distribution. The classification helps in understanding the developmental mechanisms of epithelial polarity.

📸 **Input Data:**
- TIFF images of neuroepithelial organoids stained for ZO1-EGFP

📊 **Output Data:**
- **CSV File:** Quantitative classification of cells (Apical-in/Apical-out)
- **Overlay Image:** Color-coded cell classifications (🔵 Blue = Apical-out, 🔴 Red = Apical-in)

---

## 🛠️ Project Structure

📂 **Project Files:**
```
📜 image_processing.py   # Handles image loading and preprocessing
📜 segmentation.py       # Performs segmentation and labeling
📜 classification.py     # Classifies cells into Apical-in/Apical-out
📜 utils.py              # Utility functions for saving files and computing stats
📜 main.py               # The main script to run everything
📜 requirements.txt      # List of dependencies
📜 README.md             # Project Documentation
📜 cell_classification_results.csv  # Output file
📜 cell_classification_overlay.tif  # Output image
```

---

## 🔧 Installation & Usage

💻 **Set up your environment:**
```sh
# Clone the repository
$ git clone https://github.com/fenggeshan/cell-classification.git
$ cd cell-classification

# Install dependencies
$ pip install -r requirements.txt

# Run the pipeline
$ python main.py --image /path/to/your/image.tif
```

---

## 📌 Pipeline Workflow

1️⃣ **Preprocess Image** 📷
   - Convert to grayscale
   - Apply Otsu thresholding to create a binary mask
   - Remove small objects & fill holes

2️⃣ **Segment Cells** 🔍
   - Label individual cells
   - Extract region properties

3️⃣ **Classify Cells** 🎨
   - Compute distance transform
   - Measure ZO1 fluorescence intensity
   - Apply classification rules (Apical-in / Apical-out)

4️⃣ **Generate Outputs** 📊
   - Save **CSV file** with cell measurements
   - Save **Overlay Image** for visualization

---

## 💖 Visualization

![Screenshot 2025-02-12 at 12.03.21](images/Screenshot_2025-02-12_at_12.03.21.png)

**Legend:**
- 🔵 **Blue** = Apical-out
- 🔴 **Red** = Apical-in

---

## 📌 Dependencies

- Python 3.8+
- NumPy
- SciPy
- Scikit-Image
- Pandas
- Matplotlib

To install them manually:
```sh
pip install numpy scipy scikit-image pandas matplotlib
```
