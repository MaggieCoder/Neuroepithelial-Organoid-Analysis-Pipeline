Here is a well-structured `README.md` file for your **Bioinformatics Project - Cell Classification**. It includes all the required sections and clearly explains the purpose, pipeline, and expected inputs/outputs.

---

### `README.md`
```markdown
# Apical-In/Apical-Out Cell Classification

## 📌 Biological Question
This project aims to distinguish between **Apical-In** and **Apical-Out** neuroepithelial organoid cells based on **ZO1-EGFP fluorescence intensity distribution**. The classification is based on the relative positioning of high-intensity pixels within each cell, helping to quantify apical-basal polarity changes in organoid development.

## 📝 Project Description
This project provides a **semi-automated image analysis pipeline** for classifying cells in fluorescence microscopy images. The pipeline:
- Segments individual cells based on intensity thresholds.
- Identifies **high-intensity** pixels corresponding to ZO1-EGFP signal.
- Computes spatial distributions of these pixels within cells.
- Classifies cells as **Apical-In** or **Apical-Out** based on their intensity-distance ratio.

## 📂 Project Structure
```
├── image_processing.py        # Handles image loading and preprocessing
├── segmentation.py            # Performs cell segmentation and labeling
├── classification.py          # Classifies cells into Apical-In/Apical-Out
├── utils.py                   # Utility functions for saving files and computing statistics
├── main.py                    # Main script to run the pipeline
├── requirements.txt           # List of dependencies
├── README.md                  # Project documentation
├── cell_classification_results.csv  # Output file with classification results
├── cell_classification_overlay.tif  # Output image showing classification
```

## 🛠️ Programming Environment
- **Python 3.8+**
- Developed and tested in **Jupyter Notebook** and **Standalone Python Scripts**.

## 📚 Required Python Libraries
The pipeline relies on the following scientific libraries:
- `numpy` - Array computations
- `pandas` - Data manipulation
- `matplotlib` - Visualization
- `scipy` - Mathematical computations
- `skimage` - Image processing
- `os` - File handling

To install dependencies, run:
```bash
pip install -r requirements.txt
```

## 🏗️ Additional Tools
- **Fiji/ImageJ** (optional) – for manual image verification.
- **Excel or any CSV viewer** – to analyze the classification output.

## 💻 Hardware Requirements
- A **standard laptop/desktop** with at least **8GB RAM**.
- Recommended **GPU support** for large image datasets.

---

## 📊 Input and Output Data

### 📥 Input
- **Microscopy images** in `.tif` or `.png` format.
- **ZO1-EGFP labeled fluorescence images** are required.
- The script can handle **grayscale** and **RGB images** (automatically converts RGB to grayscale).

### 📤 Output
- **`cell_classification_results.csv`**: A table containing:
  - Cell ID
  - Total area (px)
  - Apical area (high-intensity region)
  - Apical percentage
  - Mean intensity-distance ratio
  - Classification: **Apical-In / Apical-Out**

- **`cell_classification_overlay.tif`**: A visualization where:
  - **Red cells** = Apical-In
  - **Blue cells** = Apical-Out

---

## 🔬 Pipeline Workflow Overview
1. **Load Image** – Convert multi-channel images to grayscale.
2. **Preprocess Image** – Apply thresholding and remove small artifacts.
3. **Segment Cells** – Label individual cells.
4. **Extract Features** – Compute apical region size and intensity ratio.
5. **Classify Cells** – Categorize into **Apical-In** or **Apical-Out**.
6. **Save Results** – Output a classification table and an overlay image.

---

## 🚀 Running the Pipeline
To process an image, simply run:
```bash
python main.py --image_path path/to/image.tif
```
Modify parameters in `main.py` to adjust thresholds for specific datasets.

---

## 📌 Citation & Acknowledgments
If you use this pipeline in your research, please cite:
- **Feng Geshan (2025).** Apical-In/Apical-Out Cell Classification Pipeline. GitHub Repository: [GitHub Link]

Special thanks to **Dr. Gabriel Corfas' lab** for the biological framework behind this project.

---

## 📧 Contact
For questions, suggestions, or collaborations, contact **Feng Geshan** at:  
📩 **geshanfeng@umich.edu**  
🔬 University of Michigan - Ann Arbor | MCDB & Biophysics
```
