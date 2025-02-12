from skimage import filters, morphology, measure
from scipy import ndimage as ndi
import numpy as np

def segment_cells(img_gray, min_cell_area=100):
    """
    Segment cells from the grayscale image using Otsu's thresholding.

    Parameters:
        img_gray (np.ndarray): Grayscale image.
        min_cell_area (int): Minimum pixel area to consider a region as a cell.

    Returns:
        np.ndarray: Labeled image with segmented cells.
    """
    thresh = filters.threshold_otsu(img_gray)
    binary = img_gray > thresh
    filled = ndi.binary_fill_holes(binary)
    cleaned = morphology.remove_small_objects(filled, min_size=min_cell_area)
    labels = measure.label(cleaned)

    return labels