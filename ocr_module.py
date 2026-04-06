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

    text = " ".join(words)

    # Clean OCR noise
    text = text.replace("T /", "")
    text = text.replace("|", "")
    text = text.replace(";", " ")
    text = text.replace(",", " ")
    text = text.replace("  ", " ")

    return text.strip()


def extract_fields(text):

    text = text.upper()
    data = {}

    # NAME (fixed)
    name_match = re.search(
        r"NAME\s*[:\-]?\s*([A-Z ]+?)(?:\s+DOB|\s+DATE|\s+GENDER|\s+MALE|\s+FEMALE|$)",
        text
    )
    data["name"] = name_match.group(1).strip() if name_match else None

    # DOB
    dob_match = re.search(r"\b\d{2}/\d{2}/\d{4}\b", text)
    data["dob"] = dob_match.group(0) if dob_match else None

    # Aadhaar (12 digit robust)
    aadhaar_match = re.search(r"\d{12}", text.replace(" ", ""))

    # PAN
    pan_match = re.search(r"[A-Z]{5}[0-9]{4}[A-Z]", text)

    if aadhaar_match:
        data["id_number"] = aadhaar_match.group(0)
    elif pan_match:
        data["id_number"] = pan_match.group(0)
    else:
        data["id_number"] = None

    return data