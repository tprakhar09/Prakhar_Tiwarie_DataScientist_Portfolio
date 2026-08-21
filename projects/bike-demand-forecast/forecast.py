"""Forecast hourly bike demand with a time-aware evaluation split."""
from __future__ import annotations

import argparse
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error


def make_features(data: pd.DataFrame) -> pd.DataFrame:
    result = data.copy()
    timestamp = pd.to_datetime(result["datetime"])
    result["hour"] = timestamp.dt.hour
    result["day_of_week"] = timestamp.dt.dayofweek
    result["month"] = timestamp.dt.month
    result["year"] = timestamp.dt.year
    return result


def main(data_path: str) -> None:
    data = make_features(pd.read_csv(data_path)).sort_values("datetime")
    features = [column for column in ["season", "holiday", "workingday", "weather", "temp", "atemp", "humidity", "windspeed", "hour", "day_of_week", "month", "year"] if column in data]
    split_at = int(len(data) * 0.80)
    train, test = data.iloc[:split_at], data.iloc[split_at:]
    baseline = np.repeat(train["count"].mean(), len(test))
    model = RandomForestRegressor(n_estimators=300, min_samples_leaf=2, random_state=42, n_jobs=-1)
    model.fit(train[features], train["count"])
    prediction = model.predict(test[features])
    for label, values in [("Baseline", baseline), ("Random forest", prediction)]:
        mae = mean_absolute_error(test["count"], values)
        rmse = mean_squared_error(test["count"], values) ** 0.5
        print(f"{label}: MAE={mae:.1f}, RMSE={rmse:.1f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, help="Path to the Bike Sharing train.csv file")
    main(parser.parse_args().data)
