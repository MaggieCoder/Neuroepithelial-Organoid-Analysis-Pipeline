"""
Generate and plot histogram of cell sizes from segmented data.
"""

import cv2
import matplotlib.pyplot as plt


def plot_cell_size_distribution(mask):
    """Compute and plot histogram of detected cell areas."""
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    areas = [cv2.contourArea(c) for c in contours if cv2.contourArea(c) > 10]

    plt.hist(areas, bins=20, edgecolor="black")
    plt.title("Cell Size Distribution")
    plt.xlabel("Area (pixels)")
    plt.ylabel("Count")
    plt.show()
