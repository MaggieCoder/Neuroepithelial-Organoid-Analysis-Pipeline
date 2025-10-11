"""Core image processing operations for organoid analysis."""

import cv2
import numpy as np


def load_image(path):
    """Load image using OpenCV in grayscale."""
    return cv2.imread(path, cv2.IMREAD_GRAYSCALE)


def segment_cells(image):
    """Perform threshold-based segmentation."""
    _, mask = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return mask
