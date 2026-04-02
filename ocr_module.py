import easyocr
import cv2
import re

reader = easyocr.Reader(['en'], gpu=False)

def preprocess(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    return gray


def extract_text(image):

    h, w = image.shape[:2]
    crop = image[int(h*0.2):int(h*0.8), int(w*0.1):int(w*0.9)]

    processed = preprocess(crop)
    results = reader.readtext(processed)

    words = []
    for (_, text, prob) in results:
        if prob > 0.5:
            words.append(text)

    return " ".join(words)


# 🔥 NEW
def extract_fields(text):

    data = {}

    name = re.findall(r"Name[:\s]+([A-Z ]+)", text.upper())
    dob = re.findall(r"\d{2}/\d{2}/\d{4}", text)
    id_number = re.findall(r"[A-Z0-9]{8,}", text)

    data["name"] = name[0] if name else None
    data["dob"] = dob[0] if dob else None
    data["id_number"] = id_number[0] if id_number else None

    return data