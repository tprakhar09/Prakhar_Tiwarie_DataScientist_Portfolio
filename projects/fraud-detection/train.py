"""Train a baseline fraud-review prioritization model."""
import argparse
from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import average_precision_score, classification_report
from sklearn.model_selection import train_test_split


def main(data_path: str) -> None:
    data = pd.read_csv(data_path)
    features = data.drop(columns="Class")
    target = data["Class"]
    x_train, x_test, y_train, y_test = train_test_split(features, target, test_size=0.20, random_state=42, stratify=target)
    model = RandomForestClassifier(n_estimators=250, min_samples_leaf=2, class_weight="balanced", random_state=42, n_jobs=-1)
    model.fit(x_train, y_train)
    probability = model.predict_proba(x_test)[:, 1]
    threshold = 0.50
    print(f"PR-AUC: {average_precision_score(y_test, probability):.3f}")
    print(classification_report(y_test, probability >= threshold, target_names=["Legitimate", "Fraud"]))
    queue = x_test[[column for column in ["Time", "Amount"] if column in x_test]].copy()
    queue["fraud_probability"] = probability
    Path("outputs").mkdir(exist_ok=True)
    queue.sort_values("fraud_probability", ascending=False).head(100).to_csv("outputs/analyst_review_queue.csv", index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True)
    main(parser.parse_args().data)
