# 📊 Customer Churn Prediction

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=flat&logo=streamlit)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?style=flat&logo=scikit-learn)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

An end-to-end Machine Learning project that predicts whether a customer is likely to **leave a company (churn)** or **continue using its services**. The project includes data preprocessing, exploratory data analysis (EDA), classification models, model evaluation, and an interactive **Streamlit dashboard** for real-time prediction.

---

## 🚀 Live Demo

> Upload your own `.csv` and get instant predictions!

```bash
streamlit run app.py
```

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Dataset Information](#-dataset-information)
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Installation & Setup](#-installation--setup)
- [How to Use](#-how-to-use)
- [ML Models](#-machine-learning-models)
- [Model Evaluation](#-model-evaluation-metrics)
- [Screenshots](#-screenshots)
- [Future Improvements](#-future-improvements)
- [Author](#-author)
- [License](#-license)

---

## 🧠 Project Overview

Customer churn prediction is one of the most critical problems in industries like:

- 📱 Telecom
- 🏦 Banking
- 💻 SaaS Platforms
- 📦 Subscription Services

This project helps companies **identify at-risk customers** before they leave, enabling proactive retention strategies and reducing revenue loss.

---

## 📁 Dataset Information

The dataset contains customer-related information such as:

| Column | Description |
|--------|-------------|
| `Gender` | Customer gender |
| `SeniorCitizen` | Whether customer is a senior citizen |
| `Tenure` | Number of months with the company |
| `MonthlyCharges` | Monthly bill amount |
| `TotalCharges` | Total amount charged |
| `InternetService` | Type of internet service |
| `Contract` | Contract type (Month-to-month, 1 year, 2 year) |
| `PaymentMethod` | Payment method used |
| `Churn` | Target variable — Yes/No |

> You can use the [Telco Customer Churn dataset from Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn).

---

## ⭐ Features

- ✅ Upload custom churn dataset (CSV)
- ✅ Automatic data cleaning & preprocessing
- ✅ Exploratory Data Analysis (EDA) with charts
- ✅ Multiple Machine Learning models
- ✅ Real-time customer churn prediction
- ✅ Feature importance visualization
- ✅ Interactive Streamlit dashboard
- ✅ Confusion matrix & classification report

---

## 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Analysis & Manipulation |
| Matplotlib | Data Visualization |
| Scikit-learn | Machine Learning Models |
| Streamlit | Interactive Web Application |

---

## 📂 Project Structure

```
customer-churn-prediction/
│
├── app.py                  # Main Streamlit application
├── README.md               # Project documentation
├── requirements.txt        # Required Python packages
├── LICENSE                 # MIT License
│
├── dataset/
│   └── churn.csv           # Sample dataset
│
└── screenshots/
    ├── dashboard.png
    ├── graphs.png
    └── prediction.png
```

---

## ▶️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/customer-churn-prediction.git
cd customer-churn-prediction
```

### 2. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 📖 How to Use

1. **Upload** your csv file using the file uploader
2. **Explore** the dataset preview and summary statistics
3. **Analyze** EDA charts — churn distribution, contract types, monthly charges
4. **Select** a Machine Learning model from the sidebar
5. **Evaluate** model performance — accuracy, recall, ROC-AUC, confusion matrix
6. **Predict** — enter customer details and click "Predict Customer Churn"

---

## 🤖 Machine Learning Models

### Logistic Regression
- Used for binary classification (Churn: Yes / No)
- Serves as a fast, interpretable baseline model

### Random Forest Classifier
- Ensemble of 100 decision trees
- Higher accuracy with feature importance visualization

---

## 📊 Model Evaluation Metrics

| Metric | Description |
|--------|-------------|
| Accuracy | Overall correct predictions |
| Recall | True churn customers correctly identified |
| ROC-AUC | Model discrimination ability |
| Confusion Matrix | Breakdown of TP, TN, FP, FN |
| Classification Report | Precision, Recall, F1 per class |

---

## 📸 Screenshots

### Dashboard
<img width="1366" height="626" alt="image" src="https://github.com/user-attachments/assets/75c2df0f-a3e8-4ad8-8953-250254b65b0d" />
Monthly charges distribution
<img width="1161" height="865" alt="image" src="https://github.com/user-attachments/assets/55c101dd-927f-4d38-8fd9-058720293cfc" />
ROC Curve
<img width="1134" height="908" alt="image" src="https://github.com/user-attachments/assets/00de8310-a361-4f7f-a82a-a7f4a079169f" />
Feature Importance
<img width="1291" height="869" alt="image" src="https://github.com/user-attachments/assets/a9eac05e-b662-42af-9311-2ff06ecd41a6" />







---

## 🔮 Future Improvements

- [ ] Add XGBoost & Gradient Boosting classifiers
- [ ] Deploy on Streamlit Cloud
- [ ] Add downloadable prediction reports (CSV/PDF)
- [ ] Improve dashboard UI/UX
- [ ] Add user authentication system
- [ ] Add SHAP values for model explainability
- [ ] Support for more dataset formats

---

## 📚 Learning Outcomes

Through this project, the following concepts were implemented:

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering & Encoding
- Machine Learning Classification
- Model Evaluation & Metrics
- Streamlit App Development
- Data Visualization with Matplotlib

---

## 💡 Business Impact

This project can help companies to:

- 📉 Reduce customer churn rate
- 🎯 Improve targeted retention strategies
- 😊 Increase customer satisfaction
- 💰 Protect and grow business revenue

---

## 👨‍💻 Author

**Naman**

Machine Learning & Data Science Enthusiast

[![GitHub](https://img.shields.io/badge/bandawalanaman-black?style=flat&logo=github)](https://github.com/bandawalanaman)

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

> ⭐ If you found this project helpful, please give it a star!
