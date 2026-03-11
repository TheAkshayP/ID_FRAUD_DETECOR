def calculate_fraud_score(validation, blur, edge, text):

    score = 0

    # Image validation check
    if validation != "Valid Image":
        score += 30

    # Blur detection check
    if "Blur" in blur:
        score += 25

    # Edge anomaly check
    if "Possible" in edge:
        score += 25

    # OCR text length check
    if len(text.strip()) < 50:
        score += 20

    return score


def risk_level(score):

    if score <= 30:
        return "Low Risk"

    elif score <= 60:
        return "Medium Risk"

    else:
        return "High Risk"


def fraud_reasons(validation, blur, edge, text):

    reasons = []

    if validation != "Valid Image":
        reasons.append("Image resolution is too low")

    if "Blur" in blur:
        reasons.append("Blur detected in the document")

    if "Possible" in edge:
        reasons.append("Edge inconsistencies detected in the image")

    if len(text.strip()) < 50:
        reasons.append("Low OCR text extraction")

    if not reasons:
        reasons.append("No suspicious indicators detected")

    return reasons