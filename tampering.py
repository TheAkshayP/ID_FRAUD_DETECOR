import cv2
import numpy as np

def edge_analysis(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)

    density = np.sum(edges > 0) / edges.size

    # 🔥 More realistic thresholds
    if density < 0.006:
        return "Low Edge Detail"
    elif density < 0.025:
        return "Moderate Edge Structure"
    else:
        return "Normal Edge Structure"


def detect_noise(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    noise = np.std(gray)

    # 🔥 Improved noise sensitivity
    if noise > 70:
        return "High Noise"
    elif noise > 50:
        return "Moderate Noise"
    else:
        return "Normal Noise Level"