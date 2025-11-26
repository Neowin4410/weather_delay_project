import pandas as pd
from pathlib import Path

# -----------------------------------------------------
# 1️ Set up paths
# -----------------------------------------------------
base_path = Path(r"C:\Users\DELL\Documents\GitHub\NElson Air\weather_delay_project")

# Paths to your two CSVs
caa_path = base_path / "data" / "raw" / "202501_Punctuality_Statistics_Full_Analysis_Arrival_Departure.csv"
midas_path = base_path / "data" / "raw" / "midas-open_uk-hourly-weather-obs_dv-202507_station-metadata.csv"

# -----------------------------------------------------
# 2️ Load the CAA dataset
# -----------------------------------------------------
df = pd.read_csv(caa_path)

print(f" Successfully loaded '{caa_path.name}' into a DataFrame.")
print(f"DataFrame has {df.shape[0]} rows and {df.shape[1]} columns.\n")

# Print first 5 rows safely for both script and notebook
try:
    from IPython.display import display
    display(df.head())
except ImportError:
    print(df.head())

# -----------------------------------------------------
# 3️ Load the MIDAS weather station metadata
# -----------------------------------------------------
# Define correct column names for MIDAS metadata
new_column_names = [
    "src_id",
    "station_name",
    "station_file_name",
    "historic_county",
    "authority",
    "station_latitude",
    "station_longitude",
    "station_elevation",
    "first_year",
    "last_year"
]

midas_stations_df = pd.read_csv(
    midas_path,
    header=0,           # First parsed row is the header
    skiprows=48,        # Skip metadata lines at the top
    names=new_column_names,
    engine="python",
    on_bad_lines="skip"
)

print("\n Successfully loaded MIDAS station metadata.")
print(f"DataFrame has {midas_stations_df.shape[0]} rows and {midas_stations_df.shape[1]} columns.\n")

try:
    display(midas_stations_df.head())
except:
    print(midas_stations_df.head())

print("\nDataFrame Info:")
midas_stations_df.info()

# -----------------------------------------------------
# 4️ Save cleaned outputs to /data/processed
# -----------------------------------------------------
processed_path = base_path / "data" / "processed"
processed_path.mkdir(parents=True, exist_ok=True)

df.to_csv(processed_path / "caa_flights_clean.csv", index=False)
midas_stations_df.to_csv(processed_path / "midas_stations_clean.csv", index=False)

print(f"\n Cleaned datasets saved to: {processed_path}")
