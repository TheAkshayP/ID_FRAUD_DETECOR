import cv2
import numpy as np

def edge_analysis(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray,50,150)

    density = np.sum(edges>0)/edges.size

    if density < 0.01:
        return "Low Edge Detail"

    elif density < 0.03:
        return "Moderate Edge Structure"

    else:
        return "Normal Edge Structure"


def detect_noise(image):

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    noise = np.std(gray)

    if noise > 60:
        return "High Noise"

    else:
        return "Normal Noise Level"