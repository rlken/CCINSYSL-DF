# clean_data.py
import pandas as pd
import os

raw_data_path = 'raw_evidence.csv'
cleaned_data_path = 'cleaned_evidence.csv'

if not os.path.exists(raw_data_path):
    print(f"Error: '{raw_data_path}' not found. Please complete Week 1 activity first.")
    exit()

df = pd.read_csv(raw_data_path)

# Handle missing values
df.fillna('UNKNOWN', inplace=True)

# Convert timestamp column to datetime objects
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Save the cleaned data to a new CSV file
df.to_csv(cleaned_data_path, index=False)

print(f"Successfully cleaned and saved data to '{cleaned_data_path}'.")
print("\nFirst 5 rows of cleaned data:")
print(df.head())