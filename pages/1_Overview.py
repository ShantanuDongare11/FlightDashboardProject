import streamlit as st
import pandas as pd
import plotly.express as px

from utils import load_data, sidebar_filters, MONTH_ORDER

st.set_page_config(
    page_title="Overview",
    page_icon="📊",
    layout="wide"
)

df = load_data()
filtered_df = sidebar_filters(df)

st.title("📊 Dashboard Overview")
st.caption("Overview of flight operations from New York airports")

total_flights = len(filtered_df)
cancelled_flights = filtered_df["cancelled"].sum()
avg_departure_delay = filtered_df["departure_delay"].mean()
avg_arrival_delay = filtered_df["arrival_delay"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Flights", f"{total_flights:,}")
col2.metric("Cancelled Flights", f"{cancelled_flights:,}")
col3.metric("Avg Departure Delay", f"{avg_departure_delay:.2f} min")
col4.metric("Avg Arrival Delay", f"{avg_arrival_delay:.2f} min")

st.divider()

left, right = st.columns(2)

with left:

    airline_data = (
        filtered_df.groupby("airline_id")
        .size()
        .reset_index(name="Flights")
        .sort_values("Flights", ascending=False)
    )

    fig_airline = px.bar(
        airline_data,
        x="airline_id",
        y="Flights",
        color="Flights",
        text_auto=True,
        title="Flights by Airline"
    )

    fig_airline.update_layout(title_x=0.5)

    st.plotly_chart(fig_airline, use_container_width=True)

with right:

    monthly_data = (
        filtered_df.groupby("Month")
        .size()
        .reindex(MONTH_ORDER)
        .reset_index(name="Flights")
    )

    fig_month = px.line(
        monthly_data,
        x="Month",
        y="Flights",
        markers=True,
        title="Monthly Flight Trend"
    )

    fig_month.update_layout(title_x=0.5)

    st.plotly_chart(fig_month, use_container_width=True)

st.divider()

left2, right2 = st.columns(2)

with left2:

    origin_data = (
        filtered_df.groupby("origin")
        .size()
        .reset_index(name="Flights")
        .sort_values("Flights", ascending=False)
    )

    fig_origin = px.bar(
        origin_data,
        x="origin",
        y="Flights",
        color="Flights",
        text_auto=True,
        title="Flights by Origin Airport"
    )

    fig_origin.update_layout(title_x=0.5)

    st.plotly_chart(fig_origin, use_container_width=True)

with right2:

    cancel_df = pd.DataFrame({
        "Status": ["Completed", "Cancelled"],
        "Flights": [
            total_flights - cancelled_flights,
            cancelled_flights
        ]
    })

    fig_cancel = px.pie(
        cancel_df,
        names="Status",
        values="Flights",
        hole=0.65,
        title="Cancellation Analysis"
    )

    fig_cancel.update_layout(title_x=0.5)

    st.plotly_chart(fig_cancel, use_container_width=True)

st.divider()

delay_fig = px.histogram(
    filtered_df,
    x="departure_delay",
    nbins=50,
    title="Departure Delay Distribution"
)

delay_fig.update_layout(
    title_x=0.5,
    xaxis_title="Departure Delay (Minutes)",
    yaxis_title="Number of Flights"
)

st.plotly_chart(delay_fig, use_container_width=True)