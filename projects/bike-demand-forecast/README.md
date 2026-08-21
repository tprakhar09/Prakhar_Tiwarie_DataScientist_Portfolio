# Bike Rental Demand Forecast

## What this project does

This regression project estimates hourly bike-rental demand from time, season, holiday, and weather features. It compares a simple baseline with a tree-based model and reports error in understandable units.

## Real-world application

Demand forecasts help a bike-share or mobility operator plan vehicle availability and staffing. The same approach applies to staffing, inventory, deliveries, and appointment scheduling.

## What you will demonstrate

- Feature engineering from dates
- Time-aware train/test splitting
- Baseline versus model comparison
- Regression metrics: MAE and RMSE
- Interpreting forecasts as operational planning support

## Dataset

Download the Bike Sharing Demand competition data from Kaggle and save `train.csv` as `data/train.csv`. It should contain `datetime` and `count` columns.

## Run it

```bash
pip install -r requirements.txt
python forecast.py --data data/train.csv
```

## Portfolio talking point

“I built a demand-forecasting workflow that extracts calendar signals, respects time order during evaluation, and compares a baseline with a tree-based model using MAE and RMSE.”
