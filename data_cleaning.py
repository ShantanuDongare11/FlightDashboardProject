import pandas as pd

# Load dataset
df = pd.read_excel("data/flight_data.xlsx")

print("Original Shape:", df.shape)

# Remove duplicate rows
df = df.drop_duplicates()

# Create a cancellation flag
df["cancelled"] = df["departure"].isna()

# Fill missing aircraft IDs
df["aircraft_id"] = df["aircraft_id"].fillna("Unknown")

# Fill delay values with 0 for cancelled flights
df["departure_delay"] = df["departure_delay"].fillna(0)
df["arrival_delay"] = df["arrival_delay"].fillna(0)

# Fill air_time with 0
df["air_time"] = df["air_time"].fillna(0)

# Create new columns
df["Year"] = df["scheduled_departure"].dt.year
df["Month"] = df["scheduled_departure"].dt.month_name()
df["Day"] = df["scheduled_departure"].dt.day
df["Hour"] = df["scheduled_departure"].dt.hour
df["Weekday"] = df["scheduled_departure"].dt.day_name()

# Save cleaned data
df.to_excel("data/cleaned_flight_data.xlsx", index=False)

print("Cleaned Shape:", df.shape)
print("Cancelled Flights:", df["cancelled"].sum())

print("\nCleaning Completed Successfully!")