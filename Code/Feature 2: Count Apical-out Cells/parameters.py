# Parameters
min_cell_areas = [100, 50, 30, 15, 10, 5, 3]  # Try these thresholds in order
high_intensity_fraction = 0.8    # Fraction of maximum intensity to define high-intensity pixels
distance_ratio_threshold = 0.4   # Threshold for the distance ratio to classify cells
eccentricity_threshold = 0.4     # Filter out nearly circular objects (0 = perfect circle)

# Image Files
image_files = {
    "WIP006_G12A": "data/WIP006_G12A.tif",
    "WIP006_G12B": "data/WIP006_G12B.tif",
    "WIP006_G12C": "data/WIP006_G12C.tif",
    "WIP006_G12D": "data/WIP006_G12D.tif",
}