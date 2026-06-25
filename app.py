import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Heart Disease Predictor", page_icon="💓", layout="wide")

st.markdown(
    """
<style>
div[data-testid="stForm"] {
    border: none !important;
    padding: 0 !important;
    background: transparent !important;
}
</style>
""",
    unsafe_allow_html=True,
)

try:
    model = joblib.load("heart_model.pkl")
except FileNotFoundError:
    st.error("Model file not found.")
    st.stop()

# Sidebar
with st.sidebar:
    st.title("Heart Predictor")

    st.caption("Heart disease risk prediction using machine learning.")

    st.divider()

    st.markdown("### Anas Khan")

    st.markdown("""
        [![GitHub](https://img.shields.io/badge/GitHub-itsanaskhanz-black?style=for-the-badge&logo=github)](https://github.com/itsanaskhanz)

        [![LinkedIn](https://img.shields.io/badge/LinkedIn-itsanaskhanz-blue?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/itsanaskhanz)
        """)

    st.divider()

    st.caption("For educational purposes only.")

st.title("💓 Heart Disease Risk Assessment")

st.markdown("""
Estimate the likelihood of heart disease using patient clinical information.

---
""")

# Dashboard Metrics

m1, m2, m3 = st.columns(3)

with m1:
    st.metric("Features Used", "13")

with m2:
    st.metric("Model Loaded", "✔")

with m3:
    st.metric("Prediction Type", "Binary")

st.write("")

# Input Form Container
with st.container():

    st.subheader("🩺 Patient Information")

with st.form("heart_form"):

    st.markdown("### Personal Information")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", 1, 120, 40)

    with col2:
        sex = st.selectbox("Sex", ["Female", "Male"])

    st.divider()

    st.markdown("### Heart Measurements")

    col1, col2, col3 = st.columns(3)

    with col1:
        trestbps = st.number_input("Resting Blood Pressure", 50, 250, 120)

    with col2:
        chol = st.number_input("Cholesterol", 50, 700, 200)

    with col3:
        thalach = st.number_input("Maximum Heart Rate", 50, 250, 150)

    st.divider()

    st.markdown("### Clinical Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])

        fbs = st.selectbox("Fasting Blood Sugar", ["No", "Yes"])

    with col2:
        restecg = st.selectbox("Resting ECG", [0, 1, 2])

        exang = st.selectbox("Exercise Angina", ["No", "Yes"])

    with col3:
        slope = st.selectbox("Slope", [0, 1, 2])

        ca = st.selectbox("Major Vessels", [0, 1, 2, 3, 4])

        thal = st.selectbox("Thal", [0, 1, 2, 3])

    oldpeak = st.slider(
        "Oldpeak",
        min_value=0.0,
        max_value=10.0,
        value=1.0,
        step=0.1,
    )

    st.write("")

    c1, c2, c3 = st.columns([3, 1, 3])

    with c2:
        submitted = st.form_submit_button("🚀 Predict")

# Prediction
if submitted:

    input_data = pd.DataFrame(
        [
            [
                age,
                1 if sex == "Male" else 0,
                cp,
                trestbps,
                chol,
                1 if fbs == "Yes" else 0,
                restecg,
                thalach,
                1 if exang == "Yes" else 0,
                oldpeak,
                slope,
                ca,
                thal,
            ]
        ],
        columns=[
            "age",
            "sex",
            "cp",
            "trestbps",
            "chol",
            "fbs",
            "restecg",
            "thalach",
            "exang",
            "oldpeak",
            "slope",
            "ca",
            "thal",
        ],
    )

    prediction = model.predict(input_data)[0]

    st.divider()

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✔ Low Risk of Heart Disease")

    with st.expander("📋 View Submitted Data"):
        st.dataframe(input_data, use_container_width=True)
