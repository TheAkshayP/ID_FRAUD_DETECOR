def calculate_fraud_score(validation, sharpness, brightness, contrast, edge, noise, ela, text):

    score = 0

    # Validation
    if validation != "Valid Image":
        score += 15

    # Sharpness
    if sharpness < 50:
        score += 25
    elif sharpness < 80:
        score += 15

    # Brightness
    if brightness in ["Too Dark", "Too Bright"]:
        score += 10

    # Contrast
    if contrast == "Low Contrast":
        score += 10

    # Edge
    if "Low Edge" in edge:
        score += 15

    # Noise
    if "High Noise" in noise:
        score += 15

    # ELA
    if "High Compression" in ela:
        score += 20
    elif "Moderate Compression" in ela:
        score += 10

    # OCR text length
    text_len = len(text.strip())

    if text_len < 20:
        score += 20
    elif text_len < 50:
        score += 10

    # Keywords
    keywords = ["DOB", "NAME", "LICENSE", "ID"]
    keyword_count = sum(k in text.upper() for k in keywords)

    if keyword_count == 0:
        score += 20
    elif keyword_count == 1:
        score += 10

    return min(score, 100)


def risk_level(score):

    if score < 30:
        return "Low Risk"
    elif score < 60:
        return "Medium Risk"
    else:
        return "High Risk"


def fraud_reasons(validation, sharpness, brightness, contrast, edge, noise, ela, text):

    reasons = []

    if validation != "Valid Image":
        reasons.append("Low resolution image")

    if sharpness < 80:
        reasons.append("Blurry image detected")

    if brightness in ["Too Dark", "Too Bright"]:
        reasons.append("Lighting issue detected")

    if contrast == "Low Contrast":
        reasons.append("Low contrast detected")

    if "Low Edge" in edge:
        reasons.append("Edge inconsistency detected")

    if "High Noise" in noise:
        reasons.append("High noise detected")

    if "Compression" in ela:
        reasons.append("Compression artifacts detected")

    if len(text.strip()) < 40:
        reasons.append("Low OCR readability")

    keywords = ["DOB", "NAME", "LICENSE"]

    if not any(k in text.upper() for k in keywords):
        reasons.append("Important ID fields missing")

    if not reasons:
        reasons.append("No major fraud indicators detected")

    return reasons