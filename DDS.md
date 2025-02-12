---

## **📜 Design Document Specification (DDS) for Apical-in & Apical-out Classification Project**  

---

## **1️⃣ Project Overview**  
### **1.1 Purpose**  
This project aims to classify **Apical-in** and **Apical-out** cell configurations in neuroepithelial organoids based on ZO1-EGFP fluorescence intensity and spatial distribution. The tool processes `.[...]

### **1.2 Scope**  
- Load `.tif` images (grayscale or single-channel fluorescence).  
- Perform **Otsu thresholding** for segmentation.  
- Identify and label individual cells.  
- Extract intensity-based spatial features.  
- Classify each cell as **Apical-in** or **Apical-out** using a **distance ratio metric**.  
- Generate structured output data (CSV file) and a **color-coded overlay image** for visualization.  

### **1.3 System Context**  
The software operates in a **research computing environment**, primarily for analyzing microscopy images in neuroscience and organoid development studies. The system must be efficient, scalable, and f[...]

---

## **2️⃣ System Architecture**  
The system follows a **modular pipeline structure**, dividing tasks into distinct processing steps.

### **2.1 Modules and Dependencies**
The project is divided into **five core modules**, each responsible for a different aspect of the workflow:

| **Module**              | **Functionality** |
|-------------------------|-----------------------------------------------------------|
| **Image Processing**    | Load and preprocess `.tif` images (grayscale conversion, thresholding, segmentation) |
| **Cell Segmentation**   | Detect individual cells, remove noise, and extract region properties |
| **Feature Extraction**  | Compute **Euclidean Distance Transform**, identify high-intensity regions |
| **Classification**      | Determine **Apical-in** vs **Apical-out** based on intensity distance ratio |
| **Results Generation**  | Save CSV file with classification data, create and save overlay image |

---

## **3️⃣ Module Design Details**  

### **3.1 Image Processing Module**  
**Inputs:** `.tif` image  
**Processes:**  
- Convert multi-channel images to grayscale  
- Normalize pixel intensities  
- Apply **Otsu’s thresholding**  
- Perform **morphological operations** for noise reduction  

**Output:** Binary cell mask for further processing  

---

### **3.2 Cell Segmentation Module**  
**Inputs:** Binary cell mask  
**Processes:**  
- Label individual cells  
- Remove **small objects (< 100 px)**  
- Compute basic region properties (area, perimeter, bounding box)  

**Output:** Labeled cell regions for classification  

---

### **3.3 Feature Extraction Module**  
**Inputs:** Labeled cells, grayscale image  
**Processes:**  
- Compute **Euclidean Distance Transform**  
- Identify **high-intensity regions** (> 80% of max pixel value)  
- Calculate **mean distance of high-intensity pixels**  
- Compute **distance ratio** (relative position of high-intensity pixels)  

**Output:** Numeric features for classification  

---

### **3.4 Classification Module**  
**Inputs:** Extracted features (distance ratio)  
**Processes:**  
- Compare **distance ratio** to a threshold (default `0.5`)  
- Assign label:  
  - 🔴 **Apical-in** if high-intensity pixels are centrally concentrated  
  - 🔵 **Apical-out** if high-intensity pixels are near cell edges  

**Output:** Classified cell labels  

---

### **3.5 Results Generation Module**  
**Inputs:** Classified cell labels, segmented image  
**Processes:**  
- Save **CSV file** with classification data  
- Generate **color-coded overlay image**:
-![output.png](image/output.png)
  - 🔴 **Red** for Apical-in  
  - 🔵 **Blue** for Apical-out  
- Display **original vs. classified image**  

**Output:** `cell_classification_results.csv` + `cell_classification_overlay.png`  

---

## **4️⃣ Data Flow & Workflow**  
Below is a **step-by-step workflow** for the system:

```plaintext
Step 1: Load image → Convert to grayscale (if needed) → Normalize intensity
Step 2: Apply Otsu thresholding → Segment cells → Remove small objects
Step 3: Compute Distance Transform → Identify high-intensity regions
Step 4: Compute distance ratio → Classify as Apical-in / Apical-out
Step 5: Save results (CSV + overlay image) → Display output

## **5️⃣ System Constraints & Performance Considerations**  
### **5.1 Performance Requirements**  
- Image processing must complete **in under 30 seconds per image** on a standard research workstation.  
- The system must be able to process multiple images in batch mode.  

### **5.2 Hardware Requirements**  
| Component       | Minimum Specification |
|----------------|----------------------|
| **CPU**        | Intel i5 / AMD Ryzen 5 or higher |
| **RAM**        | 8GB (16GB recommended) |
| **Storage**    | 1GB free space |
| **GPU**        | Not required (but speeds up processing if available) |

### **5.3 Software Dependencies**  
- **Python 3.8+**  
- `numpy`, `matplotlib`, `scikit-image`, `scipy`, `pandas`  

---

## **6️⃣ Future Enhancements**  
🔹 **Batch Processing Mode** – Automate multi-image analysis  
🔹 **Parameter Tuning Interface** – Allow users to adjust thresholds interactively  
🔹 **Deep Learning-based Classification** – Explore AI models for more accurate classification  

---

## **7️⃣ References**  
📌 **Scikit-Image Documentation** → [scikit-image.org](https://scikit-image.org/)  
📌 **SciPy ndimage (Image Processing)** → [SciPy Docs](https://docs.scipy.org/doc/scipy/reference/ndimage.html)  
📌 **Python Data Analysis (Pandas)** → [Pandas Docs](https://pandas.pydata.org/)  
