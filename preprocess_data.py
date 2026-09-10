"""
Week 11 - Final Project: Preprocessing
Reads final_project_raw_data.csv, cleans it, and engineers new features.

Produces: final_project_cleaned_data.csv
"""

import pandas as pd

RAW_FILE = "final_project_raw_data.csv"
CLEAN_FILE = "final_project_cleaned_data.csv"

LARGE_TRANSFER_THRESHOLD_KB = 20000  # ~20 MB
AFTER_HOURS_START = 20  # 8 PM
AFTER_HOURS_END = 6     # 6 AM


def main():
    df = pd.read_csv(RAW_FILE)

    # --- Fix data types -------------------------------------------------
    # Some timestamps come in as "MM/DD/YYYY HH:MM" instead of the usual
    # "YYYY-MM-DD HH:MM:SS" -- let pandas infer the format per value.
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    # Drop rows where the timestamp truly could not be parsed
    df = df.dropna(subset=["timestamp"])

    # --- Handle missing values ------------------------------------------
    df["file_size_kb"] = pd.to_numeric(df["file_size_kb"], errors="coerce")
    median_size = df["file_size_kb"].median()
    df["file_size_kb"] = df["file_size_kb"].fillna(median_size)

    for col in ["user_id", "host_computer", "device_id", "device_type", "action", "file_name"]:
        df[col] = df[col].fillna("UNKNOWN")

    # --- Feature engineering ---------------------------------------------
    df["hour_of_day"] = df["timestamp"].dt.hour
    df["is_weekend"] = df["timestamp"].dt.dayofweek >= 5
    df["is_after_hours"] = (df["hour_of_day"] >= AFTER_HOURS_START) | (
        df["hour_of_day"] < AFTER_HOURS_END
    )
    df["file_extension"] = df["file_name"].str.extract(r"\.([a-zA-Z0-9]+)$")
    df["file_extension"] = df["file_extension"].fillna("UNKNOWN")
    df["is_large_transfer"] = df["file_size_kb"] >= LARGE_TRANSFER_THRESHOLD_KB

    # sort chronologically for a cleaner dataset
    df = df.sort_values("timestamp").reset_index(drop=True)

    df.to_csv(CLEAN_FILE, index=False)
    print(f"Saved {CLEAN_FILE} with {len(df)} rows and {len(df.columns)} columns.")


if __name__ == "__main__":
    main()
