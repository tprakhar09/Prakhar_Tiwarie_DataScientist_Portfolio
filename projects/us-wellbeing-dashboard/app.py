"""Explore aggregate U.S. wellbeing indicators; not for clinical use."""
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="U.S. Wellbeing Trends", page_icon="🌿", layout="wide")
st.title("U.S. Wellbeing Trends")
st.caption("Aggregate public-health indicators only — not clinical advice or diagnosis.")
path = Path("data/us_wellbeing.csv")
if not path.exists():
    st.info("Add data/us_wellbeing.csv. See README.md for the required tidy format.")
    st.stop()
data = pd.read_csv(path)
required = {"State", "Year", "Measure", "Value"}
if missing := required.difference(data.columns):
    st.error(f"Missing columns: {', '.join(sorted(missing))}")
    st.stop()
data["Value"] = pd.to_numeric(data["Value"], errors="coerce")
data = data.dropna(subset=["Value"])
measure = st.selectbox("Wellbeing indicator", sorted(data["Measure"].unique()))
selected = data[data["Measure"] == measure]
year = st.slider("Year", int(selected["Year"].min()), int(selected["Year"].max()), int(selected["Year"].max()))
current = selected[selected["Year"] == year].sort_values("Value", ascending=False)
st.plotly_chart(px.bar(current, x="State", y="Value", title=f"{measure} by state ({year})"), use_container_width=True)
st.plotly_chart(px.line(selected, x="Year", y="Value", color="State", title=f"Trend: {measure}"), use_container_width=True)
