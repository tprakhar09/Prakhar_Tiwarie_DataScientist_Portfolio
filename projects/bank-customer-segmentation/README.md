# Bank Customer Segmentation | BFSI

## Business problem

Banks often have broad customer bases with different service and engagement needs. This project uses clustering to identify high-level behavioral segments that can inform general financial-education or service-outreach campaigns.

## What it demonstrates

- Exploratory analysis and feature selection
- Scaling numeric variables before clustering
- Choosing a practical number of clusters with silhouette score
- Creating segment profiles that non-technical stakeholders can understand

## Dataset and run instructions

Use the UCI **Bank Marketing** dataset (`bank-full.csv`) and save it as `data/bank-full.csv`. It uses semicolon-separated values.

```bash
pip install -r requirements.txt
python segment.py --data data/bank-full.csv
```

The output, `outputs/customer_segments.csv`, contains an assigned segment and summary features. Do not use clusters for credit eligibility, pricing, or any decision that affects a person’s access to financial services. Treat them as a starting point for aggregate analysis and human review.

## Interview talking point

“I applied K-means clustering to customer engagement data, compared candidate cluster counts using silhouette score, and translated the selected groups into simple profiles for broad outreach planning.”
