"""
Main script for the Apical Polarity Analysis Pipeline.

This script coordinates the image loading, processing, and advanced
analysis steps for identifying and quantifying Apical-out cells.
"""

from noa import utils
from image import processing
from advanced import highlight, histogram


def main():
    """Entry point for the Apical Polarity Analysis pipeline."""
    print("Starting Apical Polarity Analysis...")

    # Example workflow (customize as needed)
    image_path = "data/sample_image.tif"
    img = processing.load_image(image_path)
    processed = processing.segment_cells(img)

    highlight.highlight_apical_out_cells(processed)
    histogram.plot_cell_size_distribution(processed)

    print("Analysis complete.")


if __name__ == "__main__":
    main()
