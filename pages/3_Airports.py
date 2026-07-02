import streamlit as st
import pandas as pd
import plotly.express as px

from utils import load_data, sidebar_filters

st.set_page_config(
    page_title="Airport Analysis",
    page_icon="🛫",
    layout="wide"
)

df = load_data()
filtered_df = sidebar_filters(df)

st.title("🛫 Airport Analysis")
st.caption("Analysis of origin airports, destination airports and routes")

total_origin = filtered_df["origin"].nunique()
total_destination = filtered_df["destination"].nunique()
average_distance = filtered_df["distance"].mean()
average_air_time = filtered_df["air_time"].mean()

c1, c2, c3, c4 = st.columns(4)

c1.metric("Origin Airports", total_origin)
c2.metric("Destination Airports", total_destination)
c3.metric("Average Distance", f"{average_distance:.0f}")
c4.metric("Average Air Time", f"{average_air_time:.0f} min")

st.divider()

origin_data = (
    filtered_df.groupby("origin")
    .size()
    .reset_index(name="Flights")
)

destination_data = (
    filtered_df.groupby("destination")
    .size()
    .reset_index(name="Flights")
    .sort_values("Flights", ascending=False)
    .head(10)
)

left, right = st.columns(2)

with left:

    fig1 = px.bar(
        origin_data,
        x="origin",
        y="Flights",
        color="Flights",
        text_auto=True,
        title="Flights by Origin Airport"
    )

    fig1.update_layout(title_x=0.5)

    st.plotly_chart(fig1, use_container_width=True)

with right:

    fig2 = px.bar(
        destination_data,
        x="destination",
        y="Flights",
        color="Flights",
        text_auto=True,
        title="Top Destination Airports"
    )

    fig2.update_layout(title_x=0.5)

    st.plotly_chart(fig2, use_container_width=True)

st.divider()

route_data = (
    filtered_df.groupby(["origin", "destination"])
    .size()
    .reset_index(name="Flights")
    .sort_values("Flights", ascending=False)
    .head(10)
)

distance_data = (
    filtered_df.groupby("origin")
    .agg(Average_Distance=("distance", "mean"))
    .reset_index()
)

left2, right2 = st.columns(2)

with left2:

    route_data["Route"] = route_data["origin"] + " → " + route_data["destination"]

    fig3 = px.bar(
        route_data,
        x="Route",
        y="Flights",
        color="Flights",
        text_auto=True,
        title="Top Flight Routes"
    )

    fig3.update_layout(title_x=0.5)

    st.plotly_chart(fig3, use_container_width=True)

with right2:

    fig4 = px.bar(
        distance_data,
        x="origin",
        y="Average_Distance",
        color="Average_Distance",
        text_auto=".0f",
        title="Average Distance by Origin Airport"
    )

    fig4.update_layout(title_x=0.5)

    st.plotly_chart(fig4, use_container_width=True)

st.divider()

st.subheader("Airport Statistics")

airport_table = (
    filtered_df.groupby("origin")
    .agg(
        Flights=("flight", "count"),
        Average_Distance=("distance", "mean"),
        Average_Air_Time=("air_time", "mean")
    )
    .reset_index()
)

st.dataframe(
    airport_table,
    use_container_width=True
)