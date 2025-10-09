---
title: 'Neuroepithelial-Organoid-Analysis-Pipeline: A Python tool for automated quantification of apical polarity in neuroepithelial organoids'
tags:
  - Python
  - developmental biology
  - image analysis
  - organoid
  - epithelial polarity
authors:
  - name: Geshan Feng
    orcid:0009-0007-7005-6455
    corresponding: true
    affiliation: 1
affiliations:
 - name: University of Michigan, Department of Molecular, Cellular, and Developmental Biology, Ann Arbor, MI, USA
   index: 1
date: 2025-04-17
bibliography: paper.bib
---

# Summary

The **Neuroepithelial-Organoid-Analysis-Pipeline** is an open-source Python package for **automated classification of apical polarity** in neuroepithelial organoid images.  
Apicobasal polarization is a fundamental property of epithelial tissues, influencing processes such as progenitor proliferation and lumen formation. Manual scoring of apical polarity from fluorescence microscopy is time-consuming and subjective.  
Our pipeline introduces a **fully automated, quantitative, and reproducible** approach that processes large image datasets to identify “apical-out” and “apical-in” cell configurations.

The tool integrates threshold-based segmentation, convex hull analysis, and morphological metrics to extract per-cell and per-organoid polarity measurements.  
It generates annotated images (PNG) and summary statistics (Excel) for each dataset, enabling high-throughput and reproducible morphological analysis.  
Applied to real organoid datasets, the pipeline achieved **r = 0.98 correlation** with manual annotations and <4% mean absolute error, significantly reducing analysis time from minutes per organoid to ~12 seconds per image.

# Statement of need

Quantifying apicobasal polarity is essential for understanding **neural development**, **disease modeling**, and **drug screening**.  
Existing tools like *ImageJ/Fiji* [@schindelin2012fiji] and *CellProfiler* [@carpenter2006cellprofiler] require manual tuning and correction, limiting scalability.  
Our pipeline decouples parameter selection from user input, offering **high reproducibility**, **batch processing**, and **transparent code design** suitable for both experimental biologists and computational users.

# Implementation

Developed in **Python 3.8+**, the package uses:
- **OpenCV**, **scikit-image**, **NumPy**, **pandas**, and **openpyxl**
- Modular design:  
  `main.py`, `image_preprocessor.py`, `segmenter.py`, `analyzer.py`, `exporter.py`, `parameters.py`, `utils.py`

Key methods:
- Gaussian blur and CLAHE for noise and contrast enhancement  
- Adaptive Otsu thresholding and morphological filtering  
- Convex hull area computation and polarity classification using a **distance ratio metric**,  
  where 0 ≈ apical-out and 1 ≈ apical-in.

Outputs:
1. Annotated PNG images showing apical-out (blue) and apical-in (red) cells  
2. Excel summary files with per-cell and per-organoid statistics (area, compactness, polarity index)  

# Example usage

```bash
python main.py \
  --input-dir ./raw_images/ \
  --output-dir ./results/ \
  --config parameters.py

