# U.S. Wellbeing Trends Dashboard | Healthcare

## Business problem

Public-health teams need an accessible way to explore population-level wellbeing indicators. This dashboard examines measures such as frequent mental distress, poor physical health days, physical inactivity, and access to preventive care across states and years.

## What it demonstrates

- Working with public-health indicator data
- Transparent filters and descriptive, not diagnostic, analysis
- Clear state-level and time-trend visualizations
- Communicating limitations of aggregate health data

## Dataset and run instructions

Download a public U.S. health-indicator export from the CDC PLACES or BRFSS portal and create `data/us_wellbeing.csv` with these columns: `State`, `Year`, `Measure`, and `Value`. Each row should represent one aggregate state-year-measure observation.

```bash
pip install -r requirements.txt
streamlit run app.py
```

This dashboard is for population-level exploration, not clinical advice, individual diagnosis, or treatment decisions. Any interpretation should be reviewed with public-health and domain experts.

## Interview talking point

“I built an interactive dashboard for aggregate U.S. wellbeing indicators, enabling users to compare state-level patterns over time while clearly separating descriptive public-health insights from clinical conclusions.”
