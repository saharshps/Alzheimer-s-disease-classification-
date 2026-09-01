# Alzheimer's Disease Prediction

## Project Overview

This project predicts whether a person is likely to have Alzheimer's disease using Machine Learning.

The project includes:
- Exploratory Data Analysis (EDA)
- Data preprocessing
- Multiple Machine Learning models
- Model evaluation
- Cross-validation
- Hyperparameter tuning
- ROC-AUC analysis
- Streamlit deployment

## Dataset

The dataset contains information related to demographic, lifestyle, health, and cognitive factors.

The target variable is:

- `Diagnosis`
  - `0` = No Alzheimer's
  - `1` = Alzheimer's

`PatientID` and `DoctorInCharge` were removed because they are not useful for prediction.

## Machine Learning Models

The following models were tested:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest
- Support Vector Classifier (SVC)
- AdaBoost
- Bagging Classifier
- XGBoost
- LightGBM

## Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC
- Confusion Matrix

Cross-validation and hyperparameter tuning were also performed to compare model performance.

## Final Model

LightGBM was selected as the final model based on its overall performance across the evaluation metrics.
