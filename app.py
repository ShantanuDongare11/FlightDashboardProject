import os

print(os.listdir("pages"))

import streamlit as st

from config import PAGE_CONFIG
from utils import load_css

st.set_page_config(**PAGE_CONFIG)

load_css()

st.title("✈️ Flight Departure Dashboard")

st.markdown(
    """
Welcome to the **Flight Departure Dashboard**.

This dashboard provides an interactive analysis of flight departures from New York airports using six months of flight data.

---

## Dashboard Pages

### 📊 Overview
General flight statistics and key performance indicators.

### ✈️ Airline Analysis
Analyze airline performance, delays and market share.

### 🛫 Airport Analysis
Explore origin airports, destination airports and flight routes.

### ⏱️ Delay Analysis
Analyze departure delays, arrival delays and delay patterns.

---

## Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- Tableau Public

---

## Dataset

- Total Flights : **246,209**
- Airports : **New York Area**
- Time Period : **June – December 2024**

---

### 👈 Use the navigation menu on the left to open each dashboard page.
"""
)

st.divider()

left, right = st.columns(2)

with left:

    st.info(
        """
### Project Objectives

- Monitor flight performance

- Analyze airline operations

- Identify delay patterns

- Compare airport activity

- Support operational decision making
"""
    )

with right:

    st.success(
        """
### Dashboard Features

✅ Interactive Filters

✅ KPI Cards

✅ Professional Charts

✅ Multiple Dashboard Pages

✅ Responsive Layout

✅ Data Tables
"""
    )

st.divider()

st.caption(
    "Developed as part of the Flight Dashboard Project using Streamlit and Tableau."
)