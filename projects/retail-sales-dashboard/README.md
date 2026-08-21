# Retail Sales Dashboard

## What this project does

This Streamlit dashboard turns transaction-level retail sales data into a simple decision tool. Users can filter by region and date, then view revenue, order volume, top products, and monthly sales trends.

## Real-world application

A sales manager can use the dashboard to identify high-performing regions, see which products drive revenue, and quickly spot changes in demand. It is useful for weekly sales reviews and inventory conversations.

## What you will demonstrate

- Data loading, date parsing, and input validation
- Business metrics and grouped analysis in pandas
- Interactive filtering with Streamlit
- Clear, decision-oriented visualizations with Plotly

## Dataset

Use a retail transaction CSV containing `Order Date`, `Sales`, `Region`, and `Product Name`. The Kaggle Superstore Sales dataset is a good beginner source. Save it as `data/superstore.csv`.

## Run it

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Portfolio talking point

“I translated transaction data into an interactive dashboard with filters and business KPIs, designed for a sales manager to explore performance without writing code.”
