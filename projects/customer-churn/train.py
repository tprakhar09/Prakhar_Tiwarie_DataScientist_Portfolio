"""Train a beginner-friendly customer churn classifier."""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def main(data_path: str) -> None:
    data = pd.read_csv(data_path)
    data["TotalCharges"] = pd.to_numeric(data["TotalCharges"], errors="coerce")
    data["churned"] = data["Churn"].eq("Yes").astype(int)

    drop_columns = ["Churn", "churned", "customerID"]
    features = data.drop(columns=drop_columns)
    target = data["churned"]
    numeric = features.select_dtypes(include="number").columns.tolist()
    categorical = [column for column in features.columns if column not in numeric]

    preprocess = ColumnTransformer([
        ("numeric", Pipeline([("impute", SimpleImputer(strategy="median")), ("scale", StandardScaler())]), numeric),
        ("categorical", Pipeline([("impute", SimpleImputer(strategy="most_frequent")), ("encode", OneHotEncoder(handle_unknown="ignore"))]), categorical),
    ])
    model = Pipeline([("preprocess", preprocess), ("classifier", LogisticRegression(max_iter=2000, class_weight="balanced"))])
    x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42, stratify=target)
    model.fit(x_train, y_train)
    probabilities = model.predict_proba(x_test)[:, 1]
    predictions = (probabilities >= 0.50).astype(int)
    print(f"ROC-AUC: {roc_auc_score(y_test, probabilities):.3f}")
    print(classification_report(y_test, predictions, target_names=["Stayed", "Churned"]))

    outreach = data.loc[x_test.index, ["customerID", "tenure", "MonthlyCharges", "Contract"]].copy()
    outreach["churn_probability"] = probabilities
    outreach = outreach.sort_values("churn_probability", ascending=False)
    Path("outputs").mkdir(exist_ok=True)
    outreach.to_csv("outputs/churn_outreach_list.csv", index=False)
    print("Saved outputs/churn_outreach_list.csv")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, help="Path to the Telco Customer Churn CSV file")
    main(parser.parse_args().data)
