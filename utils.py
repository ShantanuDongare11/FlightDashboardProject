import streamlit as st
import pandas as pd


MONTH_ORDER = [
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

WEEKDAY_ORDER = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]


@st.cache_data
def load_data():
    return pd.read_excel("data/cleaned_flight_data.xlsx")


def load_css():
    with open("assets/style.css") as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True
        )


def sidebar_filters(df):

    st.sidebar.header("Dashboard Filters")

    selected_airline = st.sidebar.multiselect(
        "✈️ Airline",
        sorted(df["airline_id"].unique()),
        default=sorted(df["airline_id"].unique())
    )

    selected_origin = st.sidebar.multiselect(
        "🛫 Origin Airport",
        sorted(df["origin"].unique()),
        default=sorted(df["origin"].unique())
    )

    selected_destination = st.sidebar.multiselect(
        "🛬 Destination Airport",
        sorted(df["destination"].unique()),
        default=sorted(df["destination"].unique())
    )

    selected_month = st.sidebar.multiselect(
        "📅 Month",
        MONTH_ORDER,
        default=MONTH_ORDER
    )

    selected_weekday = st.sidebar.multiselect(
        "📆 Weekday",
        WEEKDAY_ORDER,
        default=WEEKDAY_ORDER
    )

    filtered_df = df[
        (df["airline_id"].isin(selected_airline))
        & (df["origin"].isin(selected_origin))
        & (df["destination"].isin(selected_destination))
        & (df["Month"].isin(selected_month))
        & (df["Weekday"].isin(selected_weekday))
    ]

    return filtered_df


def calculate_kpis(df):

    return {
        "total_flights": len(df),
        "cancelled_flights": int(df["cancelled"].sum()),
        "departure_delay": round(df["departure_delay"].mean(), 2),
        "arrival_delay": round(df["arrival_delay"].mean(), 2),
        "average_distance": round(df["distance"].mean(), 2),
        "average_air_time": round(df["air_time"].mean(), 2),
        "total_airlines": df["airline_id"].nunique(),
        "total_origins": df["origin"].nunique(),
        "total_destinations": df["destination"].nunique()
    }


def page_header(title, subtitle):

    st.title(title)
    st.caption(subtitle)
    st.divider()