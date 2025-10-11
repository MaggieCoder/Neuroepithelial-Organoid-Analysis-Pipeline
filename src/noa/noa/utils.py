"""Utility functions for data handling and preprocessing."""

def normalize_intensity(image):
    """Normalize image intensity to the range [0, 1]."""
    return image / image.max()
