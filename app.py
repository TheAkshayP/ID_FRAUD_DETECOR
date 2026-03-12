import streamlit as st
from PIL import Image
import numpy as np

from validation import validate_image
from tampering import edge_analysis, detect_noise
from image_quality import sharpness_score, brightness_analysis, contrast_analysis
from forensics import error_level_analysis
from ocr_module import extract_text
from fraud_scoring import calculate_fraud_score, risk_level, fraud_reasons

st.set_page_config(page_title="AI ID Fraud Detection", layout="wide")

st.title("AI ID Document Fraud Detection System")

st.write(
"Upload an ID document image to analyze potential tampering using computer vision and OCR techniques."
)

st.divider()

uploaded_file = st.file_uploader("Upload ID Document", type=["jpg","jpeg","png"])

if uploaded_file:

    image = Image.open(uploaded_file)
    image_np = np.array(image)

    col1, col2 = st.columns([1.2,1])

    with col1:
        st.subheader("Uploaded Document")
        st.image(image, use_container_width=True)

    validation_result = validate_image(image_np)
    sharpness = sharpness_score(image_np)
    brightness = brightness_analysis(image_np)
    contrast = contrast_analysis(image_np)
    edge_result = edge_analysis(image_np)
    noise_result = detect_noise(image_np)
    ela_result = error_level_analysis(image_np)

    text = extract_text(image_np)

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

    with col2:

        st.subheader("Fraud Analysis")

        m1, m2 = st.columns(2)

        with m1:
            st.metric("Fraud Score", fraud_score)

        with m2:
            st.metric("Risk Level", risk)

        st.progress(fraud_score/100)

        if risk == "Low Risk":
            st.success("Document appears genuine")

        elif risk == "Medium Risk":
            st.warning("Document requires manual verification")

        else:
            st.error("High risk document detected")

    st.divider()

    col3, col4 = st.columns(2)

    with col3:

        st.subheader("Image Quality Analysis")

        st.write("Sharpness Score:", sharpness)
        st.write("Brightness:", brightness)
        st.write("Contrast:", contrast)
        st.write("Edge Structure:", edge_result)
        st.write("Noise Analysis:", noise_result)
        st.write("Compression Artifacts:", ela_result)

    with col4:

        st.subheader("OCR Extracted Text")

        if text.strip() == "":
            st.warning("No readable text detected")
        else:
            st.text_area("Extracted Text", text, height=250)

    st.divider()

    st.subheader("Analysis Explanation")

    for r in reasons:
        st.write("•", r)

st.markdown("---")
st.markdown("Made by Akshay")