"""A simple retail performance dashboard for a Superstore-style CSV."""
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Retail Sales Dashboard", page_icon="📈", layout="wide")
st.title("Retail Sales Dashboard")
data_path = Path("data/superstore.csv")
if not data_path.exists():
    st.info("Add data/superstore.csv to run this dashboard. See README.md for the expected columns.")
    st.stop()

data = pd.read_csv(data_path)
required = {"Order Date", "Sales", "Region", "Product Name"}
missing = required.difference(data.columns)
if missing:
    st.error(f"CSV is missing: {', '.join(sorted(missing))}")
    st.stop()
data["Order Date"] = pd.to_datetime(data["Order Date"], errors="coerce")
data["Sales"] = pd.to_numeric(data["Sales"], errors="coerce")
data = data.dropna(subset=["Order Date", "Sales"])

regions = st.sidebar.multiselect("Region", sorted(data["Region"].dropna().unique()), default=sorted(data["Region"].dropna().unique()))
start, end = st.sidebar.date_input("Order date", value=(data["Order Date"].min().date(), data["Order Date"].max().date()))
filtered = data[data["Region"].isin(regions) & data["Order Date"].between(pd.Timestamp(start), pd.Timestamp(end))]

orders = filtered["Order ID"].nunique() if "Order ID" in filtered else len(filtered)
left, middle, right = st.columns(3)
left.metric("Revenue", f"${filtered['Sales'].sum():,.0f}")
middle.metric("Orders", f"{orders:,}")
right.metric("Average sale", f"${filtered['Sales'].mean():,.2f}")

monthly = filtered.assign(month=filtered["Order Date"].dt.to_period("M").astype(str)).groupby("month", as_index=False)["Sales"].sum()
st.plotly_chart(px.line(monthly, x="month", y="Sales", markers=True, title="Monthly revenue"), use_container_width=True)
top_products = filtered.groupby("Product Name", as_index=False)["Sales"].sum().nlargest(10, "Sales").sort_values("Sales")
st.plotly_chart(px.bar(top_products, x="Sales", y="Product Name", orientation="h", title="Top 10 products by revenue"), use_container_width=True)
