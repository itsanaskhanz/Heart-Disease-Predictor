# Heart Disease Predictor

A machine learning project that estimates heart disease risk from patient clinical data. It includes exploratory data analysis, model training and comparison, and a Streamlit web app for interactive predictions.

**Author:** [Anas Khan](https://github.com/itsanaskhanz)

> **Disclaimer:** This project is for educational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment.

## Features

- **Exploratory data analysis** — distributions, correlations, and feature-target relationships
- **Multiple classifiers** — Logistic Regression, Naive Bayes, KNN, Decision Tree, and SVM
- **Preprocessing pipeline** — `StandardScaler` for continuous features and `OneHotEncoder` for categorical features
- **Interactive UI** — Streamlit app for entering patient details and viewing risk predictions

## Dataset

The project uses the [Heart Disease UCI dataset](https://archive.ics.uci.edu/dataset/45/heart+disease) (`data/heart.csv`), with **1,025 patient records** and **13 input features**:

| Feature | Description |
|---------|-------------|
| `age` | Age in years |
| `sex` | Sex (0 = female, 1 = male) |
| `cp` | Chest pain type (0–3) |
| `trestbps` | Resting blood pressure (mm Hg) |
| `chol` | Serum cholesterol (mg/dl) |
| `fbs` | Fasting blood sugar > 120 mg/dl (0 = no, 1 = yes) |
| `restecg` | Resting electrocardiographic results (0–2) |
| `thalach` | Maximum heart rate achieved |
| `exang` | Exercise induced angina (0 = no, 1 = yes) |
| `oldpeak` | ST depression induced by exercise relative to rest |
| `slope` | Slope of the peak exercise ST segment (0–2) |
| `ca` | Number of major vessels colored by fluoroscopy (0–4) |
| `thal` | Thalassemia (0–3) |

The target column (`target`) is binary: **0 = no heart disease**, **1 = heart disease present**.

## Model Performance

Five models were trained on an 80/20 train-test split (`random_state=42`). The SVM classifier was selected for deployment.

| Model | Accuracy | Precision | Recall | F1 |
|-------|----------|-----------|--------|-----|
| Logistic Regression | 0.770 | 0.742 | 0.793 | 0.767 |
| Naive Bayes | 0.705 | 0.690 | 0.690 | 0.690 |
| KNN | 0.738 | 0.697 | 0.793 | 0.742 |
| Decision Tree | 0.738 | 0.667 | 0.897 | 0.765 |
| **SVM** | **0.754** | **0.706** | **0.828** | **0.762** |

## Project Structure

```
Heart-Disease-Predictor/
├── app.py                  # Streamlit web application
├── main.py                 # Entry point placeholder
├── data/
│   └── heart.csv           # Dataset
├── notebooks/
│   └── analysis.ipynb      # EDA, training, and model export
├── models/                 # Trained model output (created after training)
│   └── heart_model.pkl
├── pyproject.toml          # Project dependencies
├── uv.lock                 # Locked dependency versions (uv)
└── README.md
```

## Requirements

- Python **3.13+**

## Installation

### Using uv (recommended)

```bash
git clone https://github.com/itsanaskhanz/Heart-Disease-Predictor.git
cd Heart-Disease-Predictor
uv sync
```

### Using pip

```bash
git clone https://github.com/itsanaskhanz/Heart-Disease-Predictor.git
cd Heart-Disease-Predictor
pip install -e .
```

## Usage

### 1. Train the model

Open and run `notebooks/analysis.ipynb`. The notebook performs EDA, trains all models, compares metrics, and saves the SVM pipeline to `models/heart_model.pkl`.

> The `models/` directory is not tracked in git. You must run the notebook before starting the app.

### 2. Run the web app

Start the Streamlit app (it loads the model from `models/heart_model.pkl`):

```bash
streamlit run app.py
```

The app opens in your browser. Enter patient clinical details and click **Predict** to see the risk assessment.

## Tech Stack

- **Python 3.13**
- **pandas** — data manipulation
- **scikit-learn** — preprocessing, modeling, and evaluation
- **matplotlib / seaborn** — visualization
- **Streamlit** — web interface
- **joblib** — model serialization

## License

This project is open source. See the repository for license details.

## Author

**Anas Khan**

- GitHub: [@itsanaskhanz](https://github.com/itsanaskhanz)
- LinkedIn: [itsanaskhanz](https://linkedin.com/in/itsanaskhanz)
