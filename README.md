# 🔍 AI ID Document Fraud Detection System

## Overview

This project is a prototype AI system that analyzes uploaded ID document images and generates a fraud risk report indicating whether the document appears genuine or suspicious.

The system combines **Computer Vision techniques, OCR, and rule-based risk scoring** to detect potential tampering in ID documents and produce an explainable fraud analysis.

The goal of this prototype is not perfect accuracy but to demonstrate:

* Understanding of fraud detection problems
* Ability to combine AI tools
* Logical reasoning and analysis
* Clear reporting of results

---

# 🚀 Features

* Upload an ID document image
* Image validation check
* Tampering detection using computer vision
* OCR text extraction
* Fraud risk scoring
* Explainable fraud detection report
* Interactive Streamlit dashboard

---

# 🧠 System Architecture

The system follows a multi-stage fraud detection pipeline:

Upload Image
→ Image Validation
→ Tampering Detection
→ OCR Extraction
→ Fraud Risk Scoring
→ Fraud Detection Report

---

# ⚙️ Fraud Detection Approach

The system analyzes the document using several checks.

### 1️⃣ Image Validation

The system verifies that the uploaded image has acceptable resolution and format.

### 2️⃣ Tampering Detection

Computer vision techniques are used to detect possible image manipulation.

Implemented checks:

* **Blur Detection** using Laplacian variance
* **Edge Analysis** using Canny edge detection

These checks help detect potential editing artifacts.

### 3️⃣ OCR Text Extraction

The system uses **Tesseract OCR** to extract textual information from the ID document.

Extracted text helps verify that the document contains expected information.

### 4️⃣ Fraud Risk Scoring

A rule-based scoring system evaluates potential risk indicators.

Example scoring logic:

| Indicator                | Score |
| ------------------------ | ----- |
| Invalid image resolution | +30   |
| Blur detected            | +25   |
| Edge inconsistencies     | +25   |
| Low OCR text extraction  | +20   |

The final score determines the document's risk level.

### 5️⃣ Fraud Detection Report

The system generates an interpretable report including:

* Fraud Score
* Risk Level (Low / Medium / High)
* Explanation of detected indicators

---

# 🖥️ User Interface

The system is implemented as an **interactive Streamlit dashboard**.

Users can:

1. Upload an ID document
2. View analysis results
3. Inspect OCR extracted text
4. Review the fraud detection report

---

# 🛠️ Technologies Used

* **Python**
* **OpenCV** – Image processing
* **Tesseract OCR** – Text extraction
* **Streamlit** – Interactive UI
* **NumPy** – Image processing utilities

---

# 📂 Project Structure

```
id_fraud_detector
│
├── app.py                # Main Streamlit application
├── validation.py         # Image validation checks
├── tampering.py          # Tampering detection methods
├── ocr_module.py         # OCR extraction
├── fraud_scoring.py      # Fraud scoring and reasoning
│
├── requirements.txt      # Project dependencies
└── README.md
```

---

# ▶️ How to Run the Project

### 1️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 2️⃣ Run the application

```
streamlit run app.py
```

### 3️⃣ Open the dashboard

The application will automatically open in your browser.

---

# 📊 Example Output

The system produces a structured fraud detection report:

Fraud Score: 20
Risk Level: Low Risk

Analysis Explanation:

• No suspicious indicators detected

---

# ⚠️ Limitations

This project is a **prototype system** designed to demonstrate the approach to fraud detection.

Limitations include:

* OCR accuracy depends on image quality
* Tampering detection uses heuristic checks
* Real production systems would require advanced ML models

---

# 🔮 Future Improvements

Possible improvements include:

* Deep learning based forgery detection
* Face detection and ID layout verification
* Advanced OCR field extraction
* Model-based anomaly detection
* Integration with fraud monitoring systems

---

# 👨‍💻 Author

Akshay
Data Science & Machine Learning Enthusiast
