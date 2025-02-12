import numpy as np
from skimage import measure
from scipy import ndimage as ndi

def classify_cells(labels, img_gray, distance_ratio_threshold=0.5, high_intensity_fraction=0.8):
    """
    Classifies cells as 'Apical-in' or 'Apical-out' based on intensity and distance.

    Parameters:
        labels (np.ndarray): Labeled image with segmented cells.
        img_gray (np.ndarray): Grayscale image.
        distance_ratio_threshold (float): Threshold for classification.
        high_intensity_fraction (float): Fraction of max intensity to consider "high intensity."

    Returns:
        dict: Dictionary with cell classifications and related metrics.
    """
    props = measure.regionprops(labels, intensity_image=img_gray)
    results = []

    for region in props:
        if region.area < 100:  
            continue
        
        cell_mask = labels == region.label
        dist_transform = ndi.distance_transform_edt(cell_mask)
        max_distance = np.max(dist_transform)

        cell_intensity = img_gray[cell_mask]
        intensity_threshold = high_intensity_fraction * np.max(cell_intensity)
        high_intensity_mask = cell_intensity > intensity_threshold

        mean_distance_high = np.mean(dist_transform[high_intensity_mask]) if np.sum(high_intensity_mask) > 0 else 0
        distance_ratio = mean_distance_high / max_distance if max_distance > 0 else 0

        classification = "Apical-out" if distance_ratio < distance_ratio_threshold else "Apical-in"

        results.append({
            "Cell_ID": region.label,
            "Total_Area_px": region.area,
            "Classification": classification,
            "Mean_High_Intensity_Distance_Ratio": distance_ratio
        })

    return results