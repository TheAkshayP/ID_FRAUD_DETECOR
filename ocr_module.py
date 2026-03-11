import pytesseract
import cv2
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    gray = cv2.threshold(gray,150,255,cv2.THRESH_BINARY)[1]

    pil_image = Image.fromarray(gray)

    text = pytesseract.image_to_string(pil_image)

    return text