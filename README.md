App Link: https://your-mental-health-predictor.streamlit.app/

ML Applications for Mental Health Diagnosis

A Machine Learning approach to support early identification of mental health risks.

📌 Overview

Mental health challenges affect millions of individuals worldwide, yet they often remain undetected due to stigma, lack of awareness, or limited access to proper care.
This project explores how machine learning can assist in identifying potential mental health risks based on behavioral, demographic, and psychological indicators.

Using a large dataset containing 292,364 rows and 17 features, this notebook builds and evaluates multiple ML models to predict mental health risk levels and demonstrates how such a predictive system can be deployed using Streamlit.

📂 Project Structure

- Data Preprocessing: Cleaning, handling missing values, and encoding categorical variables.
- Exploratory Data Analysis (EDA): Understanding distributions, patterns, and correlations.
- Model Building: Training multiple supervised learning models.
- Model Evaluation: Accuracy, classification metrics, and comparison.
- Deployment: Integrating the trained model into a Streamlit prediction app.

🛠️ Technologies Used

- Python (NumPy, Pandas, Matplotlib, Seaborn)
- Scikit-Learn
- XGBoost / Gradient Boosting (if included)
- TensorFlow / Keras (if DL model included)
- Streamlit (for deployment)
- Jupyter Notebook

📊 Dataset

The dataset includes demographic, behavioral, and psychological attributes such as:
- Gender
- Country
- Occupation
- Work Interest
- Social Weakness
- Family History
- Stress Levels
- Mood Swings
- Coping Struggles
- Mental Health History
- Treatment Information

These features collectively help the model identify patterns associated with low, medium, or high mental health risk.

🤖 Models Implemented

The notebook evaluates multiple machine learning models, including:
- Logistic Regression
- Random Forest Classifier
- Gradient Boosting / XGBoost

Each model is trained, tested, and compared to determine the best-performing approach.

🚀 Deployment with Streamlit

A simple user-friendly Streamlit web app is included to demonstrate real-world usage.
Users can input key attributes and receive a predicted mental health risk level.

Example workflow:
User Inputs → Preprocessing → Trained Model → Risk Prediction

🎯 Purpose of This Project

This project is intended for:

- Researchers and data scientists exploring ML in healthcare
- Mental health practitioners interested in analytical tools
- Students learning end-to-end machine learning pipelines
- Developers integrating predictive models into real applications

🔹 Disclaimer: This project is for educational and research purposes only.
It is not a diagnostic tool and should not replace professional medical judgment.
