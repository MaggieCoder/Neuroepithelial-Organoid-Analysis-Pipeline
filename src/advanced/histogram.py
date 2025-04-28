import os
import matplotlib.pyplot as plt

def plot_area_histogram(cell_data_list, image_name, save_dir):

    areas = [cell['Total Area'] for cell in cell_data_list]
    if areas:
        fig, ax = plt.subplots()
        ax.hist(areas, bins=20, color='skyblue', edgecolor='black')
        ax.set_title(f"Cell Area Distribution: {image_name}")
        ax.set_xlabel("Cell Area (pixels)")
        ax.set_ylabel("Number of Cells")

        output_path = os.path.join(save_dir, f"{image_name}_area_histogram.png")
        plt.savefig(output_path, bbox_inches='tight', dpi=300)
        plt.close(fig)
