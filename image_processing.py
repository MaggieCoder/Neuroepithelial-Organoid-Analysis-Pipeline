import numpy as np
from skimage import io, color, util

def load_image(image_path):
    """
    Load an image and convert to grayscale if necessary.

    Parameters:
        image_path (str): Path to the image file.

    Returns:
        np.ndarray: Grayscale image array.
    """
    img = io.imread(image_path)
    if img.ndim == 3:
        img_gray = color.rgb2gray(img)
    else:
        img_gray = img.astype(float) / np.max(img)
    
    return img_gray