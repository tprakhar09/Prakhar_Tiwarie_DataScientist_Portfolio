# Customer Churn Prediction

## What this project does

This beginner-friendly classification project predicts whether a telecom customer is likely to cancel their service. The result can help a retention team focus offers or support on customers at greatest risk.

## Real-world application

Churn is expensive: keeping an existing customer is often less costly than acquiring a new one. A model like this can rank customers for a retention campaign, while a simple analysis of model coefficients can highlight patterns worth investigating, such as contract type or customer tenure.

## What you will demonstrate

- Data cleaning and type conversion
- Train/test split without data leakage
- Categorical-variable encoding with a pipeline
- Logistic-regression classification and evaluation
- Turning model output into a ranked outreach list

## Dataset

Download IBM's Telco Customer Churn dataset from Kaggle and save it as `data/WA_Fn-UseC_-Telco-Customer-Churn.csv`. The expected target column is `Churn`.

## Run it

```bash
pip install -r requirements.txt
python train.py --data data/WA_Fn-UseC_-Telco-Customer-Churn.csv
```

The script writes `outputs/churn_outreach_list.csv`, a sample list of high-risk customers sorted by predicted probability. Do not use this model to automatically change a customer’s service; it is a prioritization aid for human review.

## Portfolio talking point

“I built a reproducible churn-prediction pipeline with preprocessing inside the model workflow to avoid leakage. I evaluated it with ROC-AUC and produced a ranked list that a retention team could use to prioritize outreach.”
