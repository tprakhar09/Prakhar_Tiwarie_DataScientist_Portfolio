"""Create interpretable bank-customer engagement segments."""
import argparse
from pathlib import Path

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


def main(data_path: str) -> None:
    data = pd.read_csv(data_path, sep=";")
    columns = [column for column in ["age", "balance", "duration", "campaign", "pdays", "previous"] if column in data]
    features = data[columns].copy().fillna(0)
    scaled = StandardScaler().fit_transform(features)
    scores = {k: silhouette_score(scaled, KMeans(n_clusters=k, n_init=20, random_state=42).fit_predict(scaled)) for k in range(2, 7)}
    best_k = max(scores, key=scores.get)
    model = KMeans(n_clusters=best_k, n_init=20, random_state=42)
    data["segment"] = model.fit_predict(scaled)
    print(f"Selected {best_k} segments. Silhouette scores: {scores}")
    print(data.groupby("segment")[columns].mean().round(1))
    Path("outputs").mkdir(exist_ok=True)
    data.to_csv("outputs/customer_segments.csv", index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True)
    main(parser.parse_args().data)
