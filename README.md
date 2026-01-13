# ✈️ Weather-Driven Flight Delay Prediction for UK Airports

This repository contains the complete data engineering and integration pipeline for a weather-aware flight delay prediction project. It prepares Civil Aviation Authority (CAA) flight punctuality data and UK MIDAS weather datasets, cleans and standardises them, and integrates both sources into a single modelling-ready dataset.

The project is designed for reproducibility, academic research, and future extension into machine learning and explainable AI models.

---

## 📁 Project Structure

weather_delay_project/
│
├── data/
│ ├── raw/
│ │ ├── 202501_Punctuality_Statistics_Full_Analysis_Arrival_Departure.csv
│ │ ├── midas-open_uk-hourly-weather-obs_dv-202507_station-metadata.csv
│ │ └── midas_hourly/
│ │ ├── heathrow_hourly.csv
│ │ ├── manchester_hourly.csv
│ │ ├── birmingham_hourly.csv
│ │ └── ...
│ │
│ └── processed/
│ ├── caa_flights_clean.csv
│ ├── midas_stations_clean.csv
│ ├── weather_monthly_all.csv
│ └── flights_with_stations.csv
│
├── notebooks/
│ ├── 01_data_preparation.html
│ └── 02_data_integration.html
│
├── scripts/
│ └── data_preparation.py
│
├── requirements.txt
└── README.md

yaml
Copy code

---

## 🎯 Project Objective

To build a unified, clean, and analysis-ready dataset that combines:
- UK flight punctuality statistics from the Civil Aviation Authority (CAA)
- UK weather observations from the MIDAS dataset (Met Office / UKCEH)

This dataset serves as the foundation for:
- Predictive modelling of flight delays
- Time-series forecasting
- Explainable AI (e.g. SHAP, Temporal Fusion Transformers)
- Multi-airport comparative analysis

---

## ⚙️ Data Preparation Pipeline

### 1. Flight Data Cleaning
- Loads CAA punctuality data
- Standardises column names
- Converts reporting periods to datetime
- Removes inconsistencies and missing values
- Saves cleaned version to:

data/processed/caa_flights_clean.csv

markdown
Copy code

### 2. MIDAS Station Metadata Cleaning
- Skips MIDAS metadata headers
- Renames columns for clarity
- Keeps geographic and temporal attributes
- Saves to:

data/processed/midas_stations_clean.csv

yaml
Copy code

---

## 🌦 Weather Data Integration

Using the MIDAS hourly datasets:
- Loads all airport weather files dynamically
- Detects header rows automatically
- Parses observation timestamps
- Converts hourly weather into monthly aggregated features:
  - Mean temperature
  - Wind speed
  - Visibility
  - Pressure
  - Rainfall
- Combines all airports into a single dataframe:

data/processed/weather_monthly_all.csv

yaml
Copy code

---

## 🔗 Final Data Integration

Flight and weather datasets are merged using:
- Airport identifiers
- Reporting month
- Nearest weather station

Final modelling dataset:

data/processed/flights_with_stations.csv

yaml
Copy code

This is the master dataset for all modelling and evaluation stages.

---

## 🧪 How to Run

### 1. Install dependencies

```bash
pip install pandas numpy matplotlib seaborn
(Optional for ML phase)

bash
Copy code
pip install torch lightning pytorch-forecasting
2. Run Data Preparation
bash
Copy code
python scripts/data_preparation.py
Or open:

Copy code
01_data_preparation.html
3. Run Data Integration
Open:

Copy code
02_data_integration.html
This performs:

Weather data loading

Aggregation

Flight-weather merging

📊 Outputs
File	Description
caa_flights_clean.csv	Cleaned CAA flight statistics
midas_stations_clean.csv	Cleaned MIDAS station metadata
weather_monthly_all.csv	Monthly aggregated weather features
flights_with_stations.csv	Final modelling dataset

🔬 Next Project Phases
Feature engineering

Time-series modelling

Temporal Fusion Transformer (TFT)

Explainable AI (SHAP)

Model fairness and robustness testing

Academic-ready visualisation and reporting

🧠 Academic Focus
This project is structured to support:

MSc / PhD research

Explainable AI in aviation operations

UK-focused weather impact modelling

Multi-airport comparative studies

Reproducible data science pipelines

🛠️ Tech Stack
Python 3.10+

pandas, NumPy

matplotlib, seaborn

PyTorch (optional ML phase)

PyTorch Forecasting

Lightning

Jupyter / VS Code

📌 Author
Ruth (Loveday Okoro)
MSc Data Analytics & Technologies
University of Bolton

This repository forms the data engineering backbone of the dissertation:

"Explainable Weather-Driven Flight Delay Prediction in UK Airports Using Artificial Intelligence"
