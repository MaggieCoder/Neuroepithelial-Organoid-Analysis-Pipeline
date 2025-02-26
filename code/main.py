from image_processing import load_image
from segmentation import segment_cells
from classification import classify_cells
import pandas as pd

def main(image_path):
    img_gray = load_image(image_path)
    labels = segment_cells(img_gray)
    classification_results, distance_ratio_threshold, high_intensity_fraction = classify_cells(labels, img_gray)

    # Include thresholds in the results
    for result in classification_results:
        result["Distance_Ratio_Threshold"] = distance_ratio_threshold
        result["High_Intensity_Fraction"] = high_intensity_fraction

    # Save results to CSV
    df = pd.DataFrame(classification_results)
    output_csv = "cell_classification_results.csv"
    df.to_csv(output_csv, index=False)
    print(f"Results saved to {output_csv}")

if __name__ == "__main__":
    image_path = input("Enter the image file path: ")
    main(image_path)
