import streamlit as st
from PIL import Image
import numpy as np

from validation import validate_image
from tampering import detect_blur, edge_analysis
from ocr_module import extract_text
st.title("ID Document Fraud Detection System")

uploaded_file = st.file_uploader("Upload ID Image", type=["jpg","jpeg","png"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image")

    image = np.array(image)

    validation_result = validate_image(image)

    st.subheader("Image Validation")
    st.write(validation_result)

    blur_result = detect_blur(image)
    edge_result = edge_analysis(image)

    st.subheader("Tampering Analysis")

    st.write("Blur Detection:", blur_result)
    st.write("Edge Analysis:", edge_result)

    text = extract_text(image)

    st.subheader("OCR Text Extraction")

    st.text(text)