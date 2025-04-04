#!/usr/bin/env python3
import os
import numpy as np
import cv2
import pandas as pd
import matplotlib.pyplot as plt
from skimage import io, filters, morphology, measure, color, util
from skimage.color import rgb2gray
from scipy.spatial import ConvexHull
from scipy import ndimage as ndi

# -------- Parameters --------
min_cell_areas = [100, 50, 30,15,5]
high_intensity_fraction = 0.7
distance_ratio_threshold = 0.7
eccentricity_threshold = 0.4

# -------- Define Image Files --------
image_files = {
    "WIP006_G12A":"/Users/fenggeshan/Desktop/tiff/WIP006_G12A.tif",
    "WIP006_G12B":"/Users/fenggeshan/Desktop/tiff/WIP006_G12B.tif",
    "WIP006_G12C":"/Users/fenggeshan/Desktop/tiff/WIP006_G12C.tif",
    "WIP006_G12D":"/Users/fenggeshan/Desktop/tiff/WIP006_G12D.tif",
}

def process_image(image_name, image_path, save_dir):
    img = io.imread(image_path)
    img_gray = rgb2gray(img) if img.ndim == 3 else img.astype(float) / np.max(img)

    thresh = filters.threshold_otsu(img_gray)
    binary = img_gray > thresh
    filled = ndi.binary_fill_holes(binary)

    combined_labels = np.zeros_like(img_gray, dtype=int)
    current_label = 1
    cell_data_list = []
    overlay_image = color.gray2rgb(util.img_as_ubyte(img_gray))

    apical_in_count = 0
    apical_out_count = 0

    for min_cell_area in min_cell_areas:
        cleaned = morphology.remove_small_objects(filled, min_size=min_cell_area)
        if not np.any(cleaned):
            continue

        closed = morphology.closing(cleaned, morphology.disk(10))
        dilated = morphology.binary_dilation(closed, morphology.disk(3))

        labels = measure.label(dilated)
        props = measure.regionprops(labels, intensity_image=img_gray)

        for region in props:
            if region.area < min_cell_area or region.eccentricity < eccentricity_threshold:
                continue

            cell_mask = labels == region.label
            dist_transform = ndi.distance_transform_edt(cell_mask)
            max_distance = np.max(dist_transform)
            cell_intensity = img_gray[cell_mask]
            intensity_threshold = high_intensity_fraction * np.max(cell_intensity)
            high_intensity_mask = np.zeros_like(cell_mask, dtype=bool)
            high_intensity_mask[cell_mask] = cell_intensity > intensity_threshold

            mean_distance_high = np.mean(dist_transform[high_intensity_mask]) if np.sum(high_intensity_mask) > 0 else 0
            distance_ratio = mean_distance_high / max_distance if max_distance > 0 else 0

            if distance_ratio < distance_ratio_threshold:
                cell_class = "Apical-out"
                cell_color = (0, 0, 255)
                apical_out_count += 1
            else:
                cell_class = "Apical-in"
                cell_color = (255, 0, 0)
                apical_in_count += 1

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

    # Convex Hull and Area Calculation
    convex_hull_summary = {}
    cell_coords = np.column_stack(np.where(combined_labels > 0))
    
    if cell_coords.size > 0:
        hull = ConvexHull(cell_coords)
        convex_hull_area = hull.volume if hull.volume > 0 else 1e-6

        apical_out_mask = np.all(overlay_image == [0, 0, 255], axis=-1)
        apical_in_mask = np.all(overlay_image == [255, 0, 0], axis=-1)

        apical_out_area = np.count_nonzero(apical_out_mask)
        apical_in_area = np.count_nonzero(apical_in_mask)

        apical_out_ratio = min(apical_out_area / convex_hull_area, 1.0)
        apical_in_ratio = min(apical_in_area / convex_hull_area, 1.0)

        convex_hull_summary = {
            "Image Title": image_name,
            "Convex Hull Area": convex_hull_area,
            "Apical-out Count": apical_out_count,
            "Apical-out Area": apical_out_area,
            "Apical-out / Convex Hull Area": round(apical_out_ratio, 4),
            "Apical-in Count": apical_in_count,
            "Apical-in Area": apical_in_area,
            "Apical-in / Convex Hull Area": round(apical_in_ratio, 4)
        }

        # Save PNG image to disk
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.imshow(overlay_image)
        ax.set_title(f"{image_name}: Red = Apical-in, Blue = Apical-out, Yellow = Convex Hull")
        ax.axis("off")
        hull_polygon = np.append(cell_coords[hull.vertices], [cell_coords[hull.vertices][0]], axis=0)
        ax.plot(hull_polygon[:, 1], hull_polygon[:, 0], color='yellow', linewidth=2)

        save_path = os.path.join(save_dir, f"{image_name}_overlay.png")
        plt.savefig(save_path, bbox_inches='tight')
        plt.close()

    return cell_data_list, convex_hull_summary

def main():
    all_cell_data = []
    convex_hull_list = []

    desktop_path = os.path.expanduser("~/Desktop")
    output_excel_path = os.path.join(desktop_path, "updated_cell_analysis.xlsx")

    for image_name, image_path in image_files.items():
        print(f"Processing {image_name} ...")
        cell_data, convex_summary = process_image(image_name, image_path, desktop_path)
        all_cell_data.extend(cell_data)
        convex_hull_list.append(convex_summary)

    # Export to Excel
    df_cells = pd.DataFrame(all_cell_data)
    df_convex = pd.DataFrame(convex_hull_list)

    # Create summary statistics
    total_apical_in = df_convex["Apical-in Count"].sum()
    total_apical_out = df_convex["Apical-out Count"].sum()
    mean_in_ratio = df_convex["Apical-in / Convex Hull Area"].mean()
    mean_out_ratio = df_convex["Apical-out / Convex Hull Area"].mean()

    df_summary = pd.DataFrame([{
        "Total Apical-in": total_apical_in,
        "Total Apical-out": total_apical_out,
        "Mean Apical-in / Hull": round(mean_in_ratio, 4),
        "Mean Apical-out / Hull": round(mean_out_ratio, 4)
    }])

    with pd.ExcelWriter(output_excel_path) as writer:
        df_cells.to_excel(writer, sheet_name="Cell Data", index=False)
        df_convex.to_excel(writer, sheet_name="Convex Hull Summary", index=False)
        df_summary.to_excel(writer, sheet_name="Summary", index=False)

    print(f"Analysis complete. Results and images saved to: {desktop_path}")

if __name__ == "__main__":
    main()