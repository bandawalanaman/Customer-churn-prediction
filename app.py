import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import roc_curve
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)
st.title("📊 Customer Churn Prediction")
st.write(
    """
    This project predicts whether a customer 
    is likely to leave the company or stay.
    """
)
uploaded_file = st.file_uploader(
    "Upload Customer Churn CSV File",
    type=["csv"]
)
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("📁 Dataset Preview")
    tab1, tab2, tab3 = st.tabs([
        "First 5 Rows",
        "Last 5 Rows",
        "Random Rows"
    ])
    with tab1:
        st.dataframe(df.head())
    with tab2:
        st.dataframe(df.tail())
    with tab3:
        st.dataframe(df.sample(5))
    if "customerID" in df.columns:
        df.drop("customerID", axis=1, inplace=True)
    if "TotalCharges" in df.columns:
        df["TotalCharges"] = pd.to_numeric(
            df["TotalCharges"],
            errors="coerce"
        )
    df.dropna(inplace=True)
    st.subheader("📌 Dataset Information")
    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing Values", df.isnull().sum().sum())
    st.write("### Column Names")
    st.write(df.columns.tolist())
    st.subheader("📈 Exploratory Data Analysis")
    # churn count
    st.write("### Customer Churn Count")
    churn_count = df["Churn"].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.bar(
        churn_count.index.astype(str),
        churn_count.values
    )
    ax1.set_xlabel("Churn")
    ax1.set_ylabel("Count")
    ax1.set_title("Customer Churn Distribution")
    st.pyplot(fig1)
    # contract type analysis
    if "Contract" in df.columns:
        st.write("### Contract Type vs Churn")

        contract_data = pd.crosstab(
            df["Contract"],
            df["Churn"]
        )
        fig2, ax2 = plt.subplots()
        contract_data.plot(
            kind="bar",
            ax=ax2
        )
        st.pyplot(fig2)
    # monthly charges analysis
    if "MonthlyCharges" in df.columns:
        st.write("### Monthly Charges Distribution")
        fig3, ax3 = plt.subplots()
        ax3.hist(
            df["MonthlyCharges"],
            bins=20
        )
        ax3.set_xlabel("Monthly Charges")
        ax3.set_ylabel("Customers")
        st.pyplot(fig3)
    text_columns = df.select_dtypes(
        include=["object"]
    ).columns
    encoder = LabelEncoder()
    for column in text_columns:
        df[column] = encoder.fit_transform(df[column])
    st.subheader("🧹 Processed Dataset")
    st.dataframe(df.head())
    X = df.drop("Churn", axis=1)
    y = df["Churn"]
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )
    st.sidebar.subheader("🤖 Choose Model")

    model_name = st.sidebar.selectbox(
        "Select Machine Learning Model",
        [
            "Logistic Regression",
            "Random Forest"
        ]
    )
    if model_name == "Logistic Regression":
        model = LogisticRegression(
            max_iter=1000
        )
    else:
        model = RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)[:, 1]
    accuracy = accuracy_score(
        y_test,
        predictions
    )
    recall = recall_score(
        y_test,
        predictions
    )
    roc_auc = roc_auc_score(
        y_test,
        probabilities
    )
    st.subheader("🎯 Model Performance")
    score1, score2, score3 = st.columns(3)
    score1.metric(
        "Accuracy",
        f"{accuracy:.2f}"
    )
    score2.metric(
        "Recall",
        f"{recall:.2f}"
    )
    score3.metric(
        "ROC-AUC",
        f"{roc_auc:.2f}"
    )
    st.subheader("📊 Confusion Matrix")
    matrix = confusion_matrix(
        y_test,
        predictions
    )
    matrix_df = pd.DataFrame(
        matrix,
        columns=["Predicted No","Predicted Yes"],
        index=["Actual No","Actual Yes"]
    )
    st.dataframe(matrix_df)
    st.subheader("📄 Classification Report")
    report = classification_report(
        y_test,
        predictions,
        output_dict=True
    )
    report_df = pd.DataFrame(report).transpose()
    st.dataframe(report_df)
    st.subheader("📉 ROC Curve")

    fpr, tpr, thresholds = roc_curve(
        y_test,
        probabilities
    )
    fig4, ax4 = plt.subplots()
    ax4.plot(fpr, tpr)
    ax4.set_xlabel("False Positive Rate")
    ax4.set_ylabel("True Positive Rate")
    ax4.set_title("ROC Curve")
    st.pyplot(fig4)
    if model_name == "Random Forest":
        st.subheader("⭐ Important Features")
        importance = model.feature_importances_
        importance_df = pd.DataFrame({
            "Feature": X.columns,
            "Importance": importance
        })
        importance_df = importance_df.sort_values(
            by="Importance",
            ascending=False
        )
        st.dataframe(importance_df)
        fig5, ax5 = plt.subplots()
        ax5.barh(
            importance_df["Feature"],
            importance_df["Importance"]
        )
        ax5.set_title("Feature Importance")
        st.pyplot(fig5)
    st.subheader("🧠 Predict New Customer")
    st.write(
        "Enter customer details below"
    )
    input_data = {}
    for column in X.columns:
        value = st.number_input(
            f"Enter {column}",
            value=float(X[column].mean())
        )
        input_data[column] = value
    input_df = pd.DataFrame([input_data])
    if st.button("Predict Customer Churn"):
        result = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0][1]
        if result == 1:
            st.error(
                f"""
                Customer is likely to leave the company.
                Churn Probability : {probability:.2f}
                """
            )
        else:
            st.success(
                f"""
                Customer is likely to stay with the company.
                Churn Probability : {probability:.2f}
                """
            )
else:
    st.info(
        "Please upload a customer churn CSV file to continue."
    )

