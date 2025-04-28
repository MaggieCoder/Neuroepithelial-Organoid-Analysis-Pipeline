import numpy as np
import matplotlib.pyplot as plt
from skimage import io, filters, morphology, measure, color, util
from skimage.color import rgb2gray
from scipy.spatial import ConvexHull
from scipy import ndimage as ndi
from parameters import min_cell_areas, high_intensity_fraction, distance_ratio_threshold, eccentricity_threshold

def process_image(image_name, image_path):
    # Read the image and convert to grayscale if needed
    img = io.imread(image_path)
    img_gray = rgb2gray(img) if img.ndim == 3 else img.astype(float) / np.max(img)
    
    # Initial thresholding and hole filling
    thresh = filters.threshold_otsu(img_gray)
    binary = img_gray > thresh
    filled = ndi.binary_fill_holes(binary)

    # Initialize overlay image and label storage
    combined_labels = np.zeros_like(img_gray, dtype=int)
    current_label = 1
    cell_data_list = []
    overlay_image = color.gray2rgb(util.img_as_ubyte(img_gray))

    # Process image for each min_cell_area threshold
    for min_cell_area in min_cell_areas:
        # Remove small objects using the current threshold
        cleaned = morphology.remove_small_objects(filled, min_size=min_cell_area)
        # If no objects are detected with the current threshold, skip it
        if not np.any(cleaned):
            print(f"{image_name} - No cells found with min_cell_area = {min_cell_area}")
            continue

        # Apply morphological closing and dilation to improve segmentation
        closed = morphology.closing(cleaned, morphology.disk(10))
        dilated = morphology.binary_dilation(closed, morphology.disk(3))

        # Label connected components and calculate region properties
        labels = measure.label(dilated)
        props = measure.regionprops(labels, intensity_image=img_gray)

        for region in props:
            # Skip regions that do not meet the area or shape requirements
            if region.area < min_cell_area or region.eccentricity < eccentricity_threshold:
                continue

            # Compute distance transform and high-intensity mask
            cell_mask = labels == region.label
            dist_transform = ndi.distance_transform_edt(cell_mask)
            max_distance = np.max(dist_transform)
            cell_intensity = img_gray[cell_mask]
            intensity_threshold = high_intensity_fraction * np.max(cell_intensity)
            high_intensity_mask = np.zeros_like(cell_mask, dtype=bool)
            high_intensity_mask[cell_mask] = cell_intensity > intensity_threshold

            # Calculate the mean distance for high-intensity pixels and the distance ratio
            mean_distance_high = np.mean(dist_transform[high_intensity_mask]) if np.sum(high_intensity_mask) > 0 else 0
            distance_ratio = mean_distance_high / max_distance if max_distance > 0 else 0

            # Classify cell as "Apical-out" if the distance ratio is below the threshold
            if distance_ratio >= distance_ratio_threshold:
                continue  # Skip cells classified as Apical-in

            cell_class = "Apical-out"
            cell_color = (0, 0, 255)  # Blue color for marking cells

            # Save the cell data along with the used min_cell_area threshold
            cell_data_list.append({
                "Image Title": image_name,
                "Cell ID": current_label,
                "Min Cell Area Threshold": min_cell_area,
                "Total Area": region.area,
                "Classification": cell_class,
                "Mean Intensity Ratio": distance_ratio
            })

            # Mark the cell region on the overlay image and store the label
            overlay_image[cell_mask] = cell_color
            combined_labels[cell_mask] = current_label
            current_label += 1

    # -------- Union Area and Convex Hull Calculation --------
    # Compute union cell area from combined_labels to avoid duplicate counting of overlapping pixels
    union_area = np.count_nonzero(combined_labels)
    convex_hull_summary = {}

    cell_coords = np.column_stack(np.where(combined_labels > 0))
    if cell_coords.size > 0:
        hull = ConvexHull(cell_coords)
        convex_hull_area = hull.volume
        # Ensure the ratio does not exceed 1.0
        total_area_ratio = min(union_area / convex_hull_area, 1.0) if convex_hull_area > 0 else 0

        convex_hull_summary = {
            "Image Title": image_name,
            "Union Cell Area": union_area,
            "Convex Hull Area": convex_hull_area,
            "Union Cell Area / Convex Hull Area": total_area_ratio
        }

        # Display the result image: blue regions indicate Apical-out cells, yellow shows the convex hull
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.imshow(overlay_image)
        ax.set_title(f"{image_name}: Blue = Apical-out, Yellow = Convex Hull")
        ax.axis("off")
        hull_polygon = np.append(cell_coords[hull.vertices], [cell_coords[hull.vertices][0]], axis=0)
        ax.plot(hull_polygon[:, 1], hull_polygon[:, 0], color='yellow', linewidth=2)
        plt.show()

    return cell_data_list, convex_hull_summary