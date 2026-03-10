import cv2

def detect_blur(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    score = cv2.Laplacian(gray, cv2.CV_64F).var()

    if score < 50:
        return "Blur Detected (Suspicious)"
    else:
        return "Image Clear"


def edge_analysis(image):

    edges = cv2.Canny(image,100,200)

    edge_pixels = edges.sum()

    if edge_pixels < 10000:
        return "Low Edge Details (Possible Tampering)"
    else:
        return "Normal Edge Structure"