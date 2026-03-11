import streamlit as st
from PIL import Image
import numpy as np

from validation import validate_image
from tampering import detect_blur, edge_analysis
from ocr_module import extract_text
from fraud_scoring import calculate_fraud_score, risk_level, fraud_reasons


# Page configuration
st.set_page_config(
    page_title="AI ID Fraud Detection",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 AI ID Document Fraud Detection System")

st.markdown(
"""
Upload an **ID document image** to analyze potential tampering using  
Computer Vision + OCR + Fraud Risk Scoring.
"""
)


uploaded_file = st.file_uploader("Upload ID Image", type=["jpg", "jpeg", "png"])


if uploaded_file is not None:

    image = Image.open(uploaded_file)
    image_np = np.array(image)

    col1, col2 = st.columns([1,1])

    # LEFT SIDE - IMAGE
    with col1:

        st.subheader("📄 Uploaded Document")

        st.image(image, use_column_width=True)


    # RIGHT SIDE - ANALYSIS
    with col2:

        st.subheader("⚙️ Document Analysis")

        validation_result = validate_image(image_np)
        blur_result = detect_blur(image_np)
        edge_result = edge_analysis(image_np)

        st.markdown("### Image Validation")
        st.write(validation_result)

        st.markdown("### Tampering Detection")

        st.write("Blur Detection:", blur_result)
        st.write("Edge Analysis:", edge_result)


    st.divider()

    # OCR SECTION
    st.subheader("🧾 OCR Text Extraction")

    text = extract_text(image_np)

    st.text(text[:500])


    st.divider()

    # FRAUD SCORING
    fraud_score = calculate_fraud_score(
        validation_result,
        blur_result,
        edge_result,
        text
    )

    risk = risk_level(fraud_score)

    reasons = fraud_reasons(
        validation_result,
        blur_result,
        edge_result,
        text
    )


    st.subheader("🚨 Fraud Detection Report")

    score_col, risk_col = st.columns(2)

    with score_col:
        st.metric("Fraud Score", fraud_score)

        st.progress(min(fraud_score / 100, 1.0))


    with risk_col:

        st.metric("Risk Level", risk)

        if risk == "Low Risk":
            st.success("✔ Document appears genuine")

        elif risk == "Medium Risk":
            st.warning("⚠ Document requires further verification")

        else:
            st.error("🚨 High Risk Document")


    st.divider()

    # EXPLAINABLE AI
    st.subheader("🧠 Analysis Explanation")

    for r in reasons:
        st.write("•", r)