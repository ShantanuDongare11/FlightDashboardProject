import streamlit as st
import pandas as pd
import plotly.express as px

from utils import load_data, sidebar_filters

st.set_page_config(
    page_title="Airline Analysis",
    page_icon="✈️",
    layout="wide"
)

df = load_data()
filtered_df = sidebar_filters(df)

st.title("✈️ Airline Analysis")
st.caption("Performance analysis of airlines operating from New York airports")

total_airlines = filtered_df["airline_id"].nunique()
total_flights = len(filtered_df)
avg_departure_delay = filtered_df["departure_delay"].mean()
avg_arrival_delay = filtered_df["arrival_delay"].mean()

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Airlines", total_airlines)
c2.metric("Flights", f"{total_flights:,}")
c3.metric("Avg Departure Delay", f"{avg_departure_delay:.2f} min")
c4.metric("Avg Arrival Delay", f"{avg_arrival_delay:.2f} min")

st.divider()

airline_summary = (
    filtered_df
    .groupby("airline_id")
    .agg(
        Flights=("flight", "count"),
        Departure_Delay=("departure_delay", "mean"),
        Arrival_Delay=("arrival_delay", "mean")
    )
    .reset_index()
)

left, right = st.columns(2)

with left:

    fig1 = px.bar(
        airline_summary.sort_values("Flights", ascending=False),
        x="airline_id",
        y="Flights",
        color="Flights",
        text_auto=True,
        title="Flights by Airline"
    )

    fig1.update_layout(title_x=0.5)

    st.plotly_chart(fig1, use_container_width=True)

with right:

    fig2 = px.bar(
        airline_summary.sort_values("Departure_Delay", ascending=False),
        x="airline_id",
        y="Departure_Delay",
        color="Departure_Delay",
        text_auto=".2f",
        title="Average Departure Delay"
    )

    fig2.update_layout(title_x=0.5)

    st.plotly_chart(fig2, use_container_width=True)

left2, right2 = st.columns(2)

with left2:

    fig3 = px.bar(
        airline_summary.sort_values("Arrival_Delay", ascending=False),
        x="airline_id",
        y="Arrival_Delay",
        color="Arrival_Delay",
        text_auto=".2f",
        title="Average Arrival Delay"
    )

    fig3.update_layout(title_x=0.5)

    st.plotly_chart(fig3, use_container_width=True)

with right2:

    fig4 = px.pie(
        airline_summary,
        names="airline_id",
        values="Flights",
        hole=0.6,
        title="Airline Market Share"
    )

    fig4.update_layout(title_x=0.5)

    st.plotly_chart(fig4, use_container_width=True)

st.divider()

st.subheader("Airline Statistics")

st.dataframe(
    airline_summary.sort_values("Flights", ascending=False),
    use_container_width=True
)