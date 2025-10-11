"""
Highlight typical Apical-out cells based on morphological features.
"""

import cv2


def highlight_apical_out_cells(mask):
    """Draw contours around detected Apical-out cells."""
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    highlighted = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(highlighted, contours, -1, (0, 255, 0), 2)
    print(f"Highlighted {len(contours)} potential Apical-out cells.")
    return highlighted
