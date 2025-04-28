import numpy as np

def highlight_typical_cells(overlay_image, combined_labels, cell_data_list, top_fraction=0.1):
   
    # Sort cells by distance ratio
    sorted_cells = sorted(cell_data_list, key=lambda x: x["Mean Intensity Ratio"])

    # Select top N cells
    top_n = max(1, int(len(sorted_cells) * top_fraction))
    highlighted_cells = sorted_cells[:top_n]

    # Recolor highlighted cells to gold
    for cell in highlighted_cells:
        mask = combined_labels == cell["Cell ID"]
        overlay_image[mask] = (255, 215, 0)  # Gold color

    return overlay_image
