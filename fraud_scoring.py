def calculate_fraud_score(validation,sharpness,brightness,contrast,edge,noise,ela,text):

    score = 0

    if validation != "Valid Image":
        score += 20

    if sharpness < 80:
        score += 20

    if brightness in ["Too Dark","Too Bright"]:
        score += 15

    if contrast == "Low Contrast":
        score += 10

    if "Low Edge" in edge:
        score += 15

    if "High Noise" in noise:
        score += 15

    if "High Compression" in ela:
        score += 20

    if len(text.strip()) < 40:
        score += 10

    keywords = ["DOB","NAME","LICENSE","ID"]

    if not any(k in text.upper() for k in keywords):
        score += 15

    return min(score,100)


def risk_level(score):

    if score < 30:
        return "Low Risk"

    elif score < 60:
        return "Medium Risk"

    else:
        return "High Risk"


def fraud_reasons(validation,sharpness,brightness,contrast,edge,noise,ela,text):

    reasons=[]

    if validation != "Valid Image":
        reasons.append("Image resolution too low")

    if sharpness < 80:
        reasons.append("Image appears blurry")

    if brightness in ["Too Dark","Too Bright"]:
        reasons.append("Lighting abnormal")

    if contrast == "Low Contrast":
        reasons.append("Low contrast detected")

    if "Low Edge" in edge:
        reasons.append("Edge structure abnormal")

    if "High Noise" in noise:
        reasons.append("High noise detected")

    if "High Compression" in ela:
        reasons.append("Compression artifacts detected")

    if len(text.strip()) < 40:
        reasons.append("Low OCR readability")

    keywords=["DOB","NAME","LICENSE"]

    if not any(k in text.upper() for k in keywords):
        reasons.append("Expected ID keywords missing")

    if not reasons:
        reasons.append("No suspicious indicators detected")

    return reasons