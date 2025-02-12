# **🧬 Apical-in & Apical-out Cell Classification - README Guidelines 🌱**  

## 🌟 1. **Biological Question: What Are We Trying to Answer?**  
Neuroepithelial organoids are **tiny, brain-like structures** that self-organize into different patterns. 🧠✨ But how do their cells arrange themselves?  

This project answers:  
**“Are cells in an organoid Apical-in (inside-facing) or Apical-out (outside-facing)?”** 🧐🔬  

By analyzing **ZO1-EGFP fluorescence**, we can classify each cell’s configuration. This helps researchers understand how these structures **develop, differentiate, and behave**—which is **super important** for neuroscience and regenerative medicine! 🌱💡  

---

## 🚀 2. **Programming Environment**  
This project is written in **Python 3** and runs on **Linux, macOS, or Windows**. 🖥️  

🔹 **Recommended Python Version**: `Python 3.8+`  
🔹 **Operating Systems**: Works on Mac 🖥️, Windows 💻, and Linux 🐧  

### **Installation Guide**  
1️⃣ Install **Python** (if you don’t have it) → [Download Here](https://www.python.org/downloads/)  
2️⃣ Install required Python libraries (see next section)  
3️⃣ Run the script in a terminal or Jupyter Notebook! 🚀  

---

## 🐍 3. **Python Libraries (Dependencies)**  
Before running the code, install these Python packages using **pip**:  

```bash
pip install numpy matplotlib scikit-image scipy pandas
```

🔧 **What Each Library Does?**  
📌 `numpy` – Handles mathematical operations 🧮  
📌 `matplotlib` – Plots results 📊  
📌 `scikit-image` – Image processing & segmentation 📸  
📌 `scipy` – Scientific computing 🧪  
📌 `pandas` – Saves results in easy-to-read tables 📑  

---

## 🛠️ 4. **Additional Tools Needed**  
Besides Python, you may need:  

✅ **Image Viewer** (e.g., ImageJ, Fiji, or any `.tif` viewer) 🖼️  
✅ **Jupyter Notebook** (Optional, for interactive use) 📒  
✅ **Git** (If you want to clone the repository)  

---

## 💻 5. **Hardware Requirements**  
Your computer should meet these minimum specs:  

🔹 **Processor**: Intel i5 / AMD Ryzen 5 or higher 🖥️  
🔹 **RAM**: At least **8GB** (16GB recommended for large images) 🧠  
🔹 **Storage**: 1GB+ free space (images & outputs) 💾  
🔹 **GPU**: Not required, but speeds up processing if available 🚀  

This script **does NOT require a high-end GPU**, but processing time **depends on image resolution** and the number of cells detected. 📸  

---

## 📂 6. **Input & Output Data**  

### 📥 **Input Data**  
🔹 **Image Format**: `.tif` (grayscale or single-channel fluorescent microscopy images)  
🔹 **Example Input File**: `WIP006_G10C.tif`  
🔹 **Location**: Place images in the same directory as the script **or specify the correct path**  

### 📤 **Output Data**  
✅ **CSV File (`cell_classification_results.csv`)**  
   - 📑 Lists **cell ID, area, intensity, classification**  
   - 🏆 Useful for data analysis & visualization  

✅ **Overlay Image (`cell_classification_overlay.png`)**  
   - **Red Cells** = Apical-in ❤️  
   - **Blue Cells** = Apical-out 💙  
   - **Final visual confirmation of results!** 🎨  

---

## 🔄 7. **Pipeline Workflow Overview**  

This is the **step-by-step workflow** of the script:  

1️⃣ **Load Image** 📸  
   - Reads `.tif` image (grayscale)  
   - Converts multi-channel images if needed  

2️⃣ **Preprocessing & Segmentation** ✂️  
   - Applies **Otsu’s thresholding** for segmentation  
   - Removes **small objects** (non-cell noise)  
   - Uses **morphological processing** for smoothing  

3️⃣ **Cell Identification & Feature Extraction** 🏷️  
   - Labels each cell  
   - Computes **Euclidean Distance Transform** 📏  
   - Extracts **high-intensity pixels (ZO1 signal)**  

4️⃣ **Classification** 🎯  
   - **Apical-in**: High-intensity pixels concentrated at the center 🔴  
   - **Apical-out**: High-intensity pixels near the boundary 🔵  
   - Uses a **distance ratio threshold (default = 0.5)**  

5️⃣ **Results Generation** ✅  
   - Saves **classification results** in a `.csv` file  
   - Generates **overlay image** with color-coded cells 🎨  
   - Displays side-by-side visualization of **original vs. classified image**  

---

## 📖 8. **References & Useful Links**  

📌 **Scikit-Image Documentation** → [scikit-image.org](https://scikit-image.org/)  
📌 **SciPy ndimage (Image Processing)** → [SciPy Docs](https://docs.scipy.org/doc/scipy/reference/ndimage.html)  
📌 **Matplotlib for Visualization** → [Matplotlib Docs](https://matplotlib.org/)  
📌 **Python Data Analysis (Pandas)** → [Pandas Docs](https://pandas.pydata.org/)  

---

## 🎉 **How to Run the Script?**  

### 🏃‍♂️ **Run in Terminal (Mac/Linux)**
```bash
python Apicalin&out.py
```

### 🏃‍♀️ **Run in Windows Command Prompt**
```powershell
python Apicalin&out.py
```

### 🚀 **Run in Jupyter Notebook**
```python
%run Apicalin&out.py
```

---

## 🎨 **Final Thoughts**  
Now you're all set to **classify your cells and explore neuroepithelial organization!** 🧠✨  

🔬 **Happy imaging & analyzing!** 🎉🔍  

💖 _If you have questions or ideas for improvements, feel free to contribute!_ 🚀  
