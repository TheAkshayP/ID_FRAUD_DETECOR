def calculate_fraud_score(validation, sharpness, brightness, contrast, edge, noise, ela, text):

    score = 0

    # 🔹 Validation
    if validation != "Valid Image":
        score += 20

    # 🔹 Sharpness
    if sharpness < 40:
        score += 25
    elif sharpness < 80:
        score += 15

    # 🔹 Brightness
    if brightness in ["Too Dark", "Too Bright"]:
        score += 10

    # 🔹 Contrast
    if contrast == "Low Contrast":
        score += 10
    elif contrast == "Moderate Contrast":
        score += 5

    # 🔹 Edge
    if "Low Edge" in edge:
        score += 15

    # 🔹 Noise
    if "High Noise" in noise:
        score += 20
    elif "Moderate Noise" in noise:
        score += 10

    # 🔹 ELA
    if "High Compression" in ela:
        score += 25
    elif "Moderate Compression" in ela:
        score += 10

    # 🔹 OCR Quality
    text_len = len(text.strip())

    if text_len < 20:
        score += 25
    elif text_len < 50:
        score += 10

    # 🔹 Keyword validation
    keywords = ["DOB", "NAME", "ID", "LICENSE"]
    keyword_count = sum(k in text.upper() for k in keywords)

    if keyword_count == 0:
        score += 25
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
        reasons.append("Blurry or low sharpness detected")

    if brightness in ["Too Dark", "Too Bright"]:
        reasons.append("Lighting anomaly detected")

    if contrast == "Low Contrast":
        reasons.append("Low contrast detected")

    if "Low Edge" in edge:
        reasons.append("Edge structure inconsistency")

    if "High Noise" in noise:
        reasons.append("High noise detected")
    elif "Moderate Noise" in noise:
        reasons.append("Moderate noise detected")

    if "Compression" in ela:
        reasons.append("Compression artifacts detected")

    if len(text.strip()) < 40:
        reasons.append("Low OCR readability")

    keywords = ["DOB", "NAME", "LICENSE"]

    if not any(k in text.upper() for k in keywords):
        reasons.append("Missing important ID fields")

    if not reasons:
        reasons.append("No suspicious indicators detected")

    return reasons