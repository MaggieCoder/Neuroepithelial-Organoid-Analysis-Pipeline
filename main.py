from image_processing import load_image
from segmentation import segment_cells
from classification import classify_cells
import pandas as pd

def main(image_path):
    img_gray = load_image(image_path)
    labels = segment_cells(img_gray)
    classification_results = classify_cells(labels, img_gray)

    # Save results to CSV
    df = pd.DataFrame(classification_results)
    output_csv = "cell_classification_results.csv"
    df.to_csv(output_csv, index=False)
    print(f"Results saved to {output_csv}")

if __name__ == "__main__":
    image_path = input("Enter the image file path: ")
    main(image_path)