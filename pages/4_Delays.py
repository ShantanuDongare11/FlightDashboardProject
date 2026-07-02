import streamlit as st
import pandas as pd
import plotly.express as px

from utils import load_data, sidebar_filters, MONTH_ORDER, WEEKDAY_ORDER

st.set_page_config(
    page_title="Delay Analysis",
    page_icon="⏱️",
    layout="wide"
)

df = load_data()
filtered_df = sidebar_filters(df)

st.title("⏱️ Delay Analysis")
st.caption("Analysis of departure delays and arrival delays")

max_departure_delay = filtered_df["departure_delay"].max()
avg_departure_delay = filtered_df["departure_delay"].mean()
avg_arrival_delay = filtered_df["arrival_delay"].mean()

on_time_flights = (
    filtered_df["departure_delay"]
    .fillna(0)
    .le(0)
    .sum()
)

c1, c2, c3, c4 = st.columns(4)

c1.metric(
    "Maximum Delay",
    f"{max_departure_delay:.0f} min"
)

c2.metric(
    "Average Departure Delay",
    f"{avg_departure_delay:.2f} min"
)

c3.metric(
    "Average Arrival Delay",
    f"{avg_arrival_delay:.2f} min"
)

c4.metric(
    "On-Time Flights",
    f"{on_time_flights:,}"
)

st.divider()

left, right = st.columns(2)

with left:

    fig_departure = px.histogram(
        filtered_df,
        x="departure_delay",
        nbins=50,
        color_discrete_sequence=["#2563EB"],
        title="Departure Delay Distribution"
    )

    fig_departure.update_layout(
        title_x=0.5,
        xaxis_title="Departure Delay (Minutes)",
        yaxis_title="Number of Flights"
    )

    st.plotly_chart(
        fig_departure,
        use_container_width=True
    )

with right:

    fig_arrival = px.histogram(
        filtered_df,
        x="arrival_delay",
        nbins=50,
        color_discrete_sequence=["#16A34A"],
        title="Arrival Delay Distribution"
    )

    fig_arrival.update_layout(
        title_x=0.5,
        xaxis_title="Arrival Delay (Minutes)",
        yaxis_title="Number of Flights"
    )

    st.plotly_chart(
        fig_arrival,
        use_container_width=True
    )

st.divider()
left2, right2 = st.columns(2)

with left2:

    weekday_delay = (
        filtered_df.groupby("Weekday")["departure_delay"]
        .mean()
        .reindex(WEEKDAY_ORDER)
        .reset_index()
    )

    fig_weekday = px.bar(
        weekday_delay,
        x="Weekday",
        y="departure_delay",
        color="departure_delay",
        text_auto=".2f",
        title="Average Departure Delay by Weekday"
    )

    fig_weekday.update_layout(
        title_x=0.5,
        xaxis_title="Weekday",
        yaxis_title="Average Delay (Minutes)"
    )

    st.plotly_chart(
        fig_weekday,
        use_container_width=True
    )

with right2:

    month_delay = (
        filtered_df.groupby("Month")["departure_delay"]
        .mean()
        .reindex(MONTH_ORDER)
        .reset_index()
    )

    fig_month = px.line(
        month_delay,
        x="Month",
        y="departure_delay",
        markers=True,
        title="Average Departure Delay by Month"
    )

    fig_month.update_layout(
        title_x=0.5,
        xaxis_title="Month",
        yaxis_title="Average Delay (Minutes)"
    )

    st.plotly_chart(
        fig_month,
        use_container_width=True
    )

st.divider()

st.subheader("Top 20 Most Delayed Flights")

top_delays = (
    filtered_df[
        [
            "flight",
            "airline_id",
            "origin",
            "destination",
            "departure_delay",
            "arrival_delay"
        ]
    ]
    .sort_values("departure_delay", ascending=False)
    .head(20)
)

st.dataframe(
    top_delays,
    use_container_width=True
)

st.divider()

st.subheader("Delay Statistics")

delay_statistics = (
    filtered_df[["departure_delay", "arrival_delay"]]
    .describe()
    .round(2)
)

st.dataframe(
    delay_statistics,
    use_container_width=True
)