import cv2
import numpy as np

def sharpness_score(image):

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    score = cv2.Laplacian(gray,cv2.CV_64F).var()

    return round(score,2)


def brightness_analysis(image):

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    brightness = np.mean(gray)

    if brightness < 70:
        return "Too Dark"

    elif brightness > 200:
        return "Too Bright"

    else:
        return "Normal Lighting"


def contrast_analysis(image):

    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    contrast = gray.std()

    if contrast < 40:
        return "Low Contrast"

    else:
        return "Normal Contrast"