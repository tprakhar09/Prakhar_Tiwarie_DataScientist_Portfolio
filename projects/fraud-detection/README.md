# Card Fraud Detection | BFSI

## Business problem

Card issuers need to spot suspicious transactions quickly while avoiding unnecessary friction for legitimate customers. This project trains a baseline model to rank transactions for a fraud analyst’s review queue.

## What it demonstrates

- Working with a severely imbalanced target
- Leakage-aware train/test splitting
- Precision, recall, PR-AUC, and threshold selection
- A ranked review queue instead of an automatic decline decision

## Dataset and run instructions

Download the Kaggle **Credit Card Fraud Detection** dataset and save it as `data/creditcard.csv`.

```bash
pip install -r requirements.txt
python train.py --data data/creditcard.csv
```

The script saves `outputs/analyst_review_queue.csv` with the highest-risk test transactions. This is a learning project only: production fraud systems require monitoring, privacy controls, secure data handling, and human oversight.

## Interview talking point

“I treated fraud detection as an imbalanced classification problem, evaluated precision and recall instead of accuracy, and generated a ranked analyst-review queue rather than automating a transaction decision.”
