#!/usr/bin/env python3
import os
import pandas as pd
from parameters import image_files
from image_processing import process_image

def main():
    all_cell_data = []
    convex_hull_list = []

    for image_name, image_path in image_files.items():
        print(f"Processing {image_name} ...")
        cell_data, convex_summary = process_image(image_name, image_path)
        all_cell_data.extend(cell_data)
        convex_hull_list.append(convex_summary)

    # -------- Save Results to Excel --------
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