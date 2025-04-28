import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from skimage import io, filters, morphology, measure, color, util
from skimage.color import rgb2gray
from scipy import ndimage as ndi
from scipy.spatial import ConvexHull

# -------- Parameters --------
min_cell_areas = [100, 50, 30, 15, 10, 5, 3, 1]
eccentricity_threshold = 0.0
high_intensity_fraction = 0.9
distance_ratio_threshold = 0.9

# -------- Image Paths --------
image_files = {

}

def otsu_threshold(image):
    """
    Apply Otsu's thresholding method to the input image.
    
    Parameters:
        image (ndarray): Input image array.
        
    Returns:
        filled (ndarray): Binary image after thresholding and hole filling.
        thresh (float): Otsu threshold value.
    """
    # Convert to grayscale if the image is in color
    if image.ndim == 3:
        img_gray = color.rgb2gray(image)
    else:
        img_gray = image.astype(float) / np.max(image)
    
    # Compute Otsu threshold and generate a binary image
    thresh = filters.threshold_otsu(img_gray)
    binary = img_gray > thresh
    
    # Fill holes in the binary image
    filled = ndi.binary_fill_holes(binary)
    
    return filled, thresh

def process_image(image_name, image_path):
    """
    Process the image to perform cell segmentation, classification, and convex hull analysis.
    
    Parameters:
        image_name (str): Title of the image.
        image_path (str): Path to the image file.
        
    Returns:
        cell_data_list (list): List of dictionaries with cell analysis data.
        convex_hull_summary (dict): Dictionary summarizing the convex hull analysis.
    """
    # Read the image
    img = io.imread(image_path)
    
    # Convert to grayscale
    img_gray = rgb2gray(img) if img.ndim == 3 else img.astype(float) / np.max(img)
    
    # Apply Otsu thresholding
    filled, thresh = otsu_threshold(img)
    print(f"{image_name} - Otsu Threshold: {thresh}")
    
    # Initialize variables for cell labeling and overlay image
    combined_labels = np.zeros_like(img_gray, dtype=int)
    current_label = 1
    cell_data_list = []
    overlay_image = color.gray2rgb(util.img_as_ubyte(img_gray))
    
    # Loop through different minimum cell area thresholds
    for min_cell_area in min_cell_areas:
        # Remove small objects based on the current threshold
        cleaned = morphology.remove_small_objects(filled, min_size=min_cell_area)
        if not np.any(cleaned):
            print(f"{image_name} - No cells found with min_cell_area = {min_cell_area}")
            continue

        # Apply morphological closing and dilation
        closed = morphology.closing(cleaned, morphology.disk(10))
        dilated = morphology.binary_dilation(closed, morphology.disk(3))

        # Label connected regions
        labels = measure.label(dilated)
        props = measure.regionprops(labels, intensity_image=img_gray)

        for region in props:
            # Filter regions by area and eccentricity
            if region.area < min_cell_area or region.eccentricity < eccentricity_threshold:
                continue

            cell_mask = labels == region.label
            # Compute distance transform for the cell mask
            dist_transform = ndi.distance_transform_edt(cell_mask)
            max_distance = np.max(dist_transform)
            cell_intensity = img_gray[cell_mask]
            intensity_threshold = high_intensity_fraction * np.max(cell_intensity)
            high_intensity_mask = np.zeros_like(cell_mask, dtype=bool)
            high_intensity_mask[cell_mask] = cell_intensity > intensity_threshold

            mean_distance_high = np.mean(dist_transform[high_intensity_mask]) if np.sum(high_intensity_mask) > 0 else 0
            distance_ratio = mean_distance_high / max_distance if max_distance > 0 else 0

            # Exclude cells with a high distance ratio
            if distance_ratio >= distance_ratio_threshold:
                continue

            # Classify cell and record cell data
            cell_class = "Apical-out"
            cell_color = (0, 0, 255)  # Blue in BGR for visualization

            cell_data_list.append({
                "Image Title": image_name,
                "Cell ID": current_label,
                "Min Cell Area Threshold": min_cell_area,
                "Total Area": region.area,
                "Classification": cell_class,
                "Mean Intensity Ratio": distance_ratio
            })

            overlay_image[cell_mask] = cell_color
            combined_labels[cell_mask] = current_label
            current_label += 1

    # Compute convex hull for the union of all detected cells
    union_area = np.count_nonzero(combined_labels)
    convex_hull_summary = {}
    cell_coords = np.column_stack(np.where(combined_labels > 0))
    if cell_coords.size > 0:
        hull = ConvexHull(cell_coords)
        convex_hull_area = hull.volume
        total_area_ratio = min(union_area / convex_hull_area, 1.0) if convex_hull_area > 0 else 0

        convex_hull_summary = {
            "Image Title": image_name,
            "Union Cell Area": union_area,
            "Convex Hull Area": convex_hull_area,
            "Union Cell Area / Convex Hull Area": total_area_ratio
        }

        # Plot overlay image with convex hull outline
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.imshow(overlay_image)
        ax.set_title(f"{image_name}: Blue = Apical-out, Yellow = Convex Hull")
        ax.axis("off")
        hull_polygon = np.append(cell_coords[hull.vertices], [cell_coords[hull.vertices][0]], axis=0)
        ax.plot(hull_polygon[:, 1], hull_polygon[:, 0], color='yellow', linewidth=2)

        # Save the plot to the desktop
        desktop_path = os.path.expanduser("~/Desktop")
        output_png_path = os.path.join(desktop_path, f"{image_name}_analysis.png")
        plt.savefig(output_png_path, bbox_inches='tight', dpi=300)
        plt.close(fig)

    return cell_data_list, convex_hull_summary

def main():
    """
    Main function to process all images and export the analysis results to an Excel file.
    """
    all_cell_data = []
    convex_hull_list = []

    for image_name, image_path in image_files.items():
        print(f"Processing {image_name} ...")
        cell_data, convex_summary = process_image(image_name, image_path)
        all_cell_data.extend(cell_data)
        convex_hull_list.append(convex_summary)

    # Save analysis results to an Excel file on the desktop
    desktop_path = os.path.expanduser("~/Desktop")
    output_excel_path = os.path.join(desktop_path, "updated_cell_analysis.xlsx")
    df_cells = pd.DataFrame(all_cell_data)
    df_convex = pd.DataFrame(convex_hull_list)

    with pd.ExcelWriter(output_excel_path) as writer:
        df_cells.to_excel(writer, sheet_name="Cell Data", index=False)
        df_convex.to_excel(writer, sheet_name="Convex Hull Summary", index=False)

    print(f"Analysis complete. Results saved to: {output_excel_path}")

if __name__ == "__main__":
    main()
    