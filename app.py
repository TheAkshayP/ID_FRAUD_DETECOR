import streamlit as st
from PIL import Image
import numpy as np

from validation import validate_image
from tampering import edge_analysis, detect_noise
from image_quality import sharpness_score, brightness_analysis, contrast_analysis
from forensics import error_level_analysis
from ocr_module import extract_text, extract_fields
from fraud_scoring import calculate_fraud_score, risk_level, fraud_reasons

st.set_page_config(page_title="AI ID Fraud Detection", layout="wide")

st.title("🚀 AI ID Document Fraud Detection System")

uploaded_file = st.file_uploader("Upload ID Document", type=["jpg","jpeg","png"])

if uploaded_file:

    image = Image.open(uploaded_file)
    image_np = np.array(image)

    st.image(image, caption="Uploaded Document")

    # Features
    validation_result = validate_image(image_np)
    sharpness = sharpness_score(image_np)
    brightness = brightness_analysis(image_np)
    contrast = contrast_analysis(image_np)
    edge_result = edge_analysis(image_np)
    noise_result = detect_noise(image_np)
    ela_result = error_level_analysis(image_np)

    text = extract_text(image_np)
    fields = extract_fields(text)

    fraud_score = calculate_fraud_score(
        validation_result,
        sharpness,
        brightness,
        contrast,
        edge_result,
        noise_result,
        ela_result,
        text
    )

    risk = risk_level(fraud_score)

    reasons = fraud_reasons(
        validation_result,
        sharpness,
        brightness,
        contrast,
        edge_result,
        noise_result,
        ela_result,
        text
    )

    st.subheader("📊 Fraud Analysis")
    st.metric("Fraud Score", fraud_score)
    st.metric("Risk Level", risk)

    st.progress(fraud_score / 100)

    st.subheader("🧠 Extracted Fields")
    st.write(fields)

    st.subheader("📄 OCR Text")
    st.text_area("Text", text, height=200)

    st.subheader("📈 Image Analysis")
    st.write({
        "Sharpness": sharpness,
        "Brightness": brightness,
        "Contrast": contrast,
        "Edge": edge_result,
        "Noise": noise_result,
        "ELA": ela_result
    })

    st.subheader("⚠️ Reasons")
    for r in reasons:
        st.write("•", r)

st.markdown("---")
st.markdown("Made by Akshay 🚀")