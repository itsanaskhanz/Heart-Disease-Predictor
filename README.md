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

The target column (`target`) is binary: **0 = no heart disease**, **1 = heart disease present**.

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
