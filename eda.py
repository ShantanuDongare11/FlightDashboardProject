import pandas as pd

# Load cleaned dataset
df = pd.read_excel("data/cleaned_flight_data.xlsx")

print("=" * 60)
print("TOTAL FLIGHTS")
print(len(df))

print("=" * 60)
print("CANCELLED FLIGHTS")
print(df["cancelled"].sum())

print("=" * 60)
print("AVERAGE DEPARTURE DELAY")
print(round(df["departure_delay"].mean(), 2))

print("=" * 60)
print("AVERAGE ARRIVAL DELAY")
print(round(df["arrival_delay"].mean(), 2))

print("=" * 60)
print("TOP 10 AIRLINES")
print(df["airline_id"].value_counts().head(10))

print("=" * 60)
print("TOP 10 ORIGIN AIRPORTS")
print(df["origin"].value_counts().head(10))

print("=" * 60)
print("TOP 10 DESTINATION AIRPORTS")
print(df["destination"].value_counts().head(10))

print("=" * 60)
print("TOP 10 MONTHS")
print(df["Month"].value_counts())

print("=" * 60)
print("TOP 10 WEEKDAYS")
print(df["Weekday"].value_counts())

print("=" * 60)
print("AVERAGE AIR TIME")
print(round(df["air_time"].mean(), 2))

print("=" * 60)
print("AVERAGE DISTANCE")
print(round(df["distance"].mean(), 2))