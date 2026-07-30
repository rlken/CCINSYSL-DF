# feature_engineer.py
import pandas as pd
import os

cleaned_data_path = 'cleaned_evidence.csv'
feature_engineered_path = 'feature_engineered_evidence.csv'

if not os.path.exists(cleaned_data_path):
    print(f"Error: '{cleaned_data_path}' not found. Please complete Week 2 activity first.")
    exit()

df = pd.read_csv(cleaned_data_path)

# Convert timestamp column back to datetime object (in case it was saved as a string)
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Feature engineering: extract useful features from the timestamp
df['hour_of_day'] = df['timestamp'].dt.hour
df['day_of_week'] = df['timestamp'].dt.day_name()
df['is_weekend'] = df['timestamp'].dt.dayofweek >= 5  # Saturday=5, Sunday=6

# Save the feature-engineered data to a new CSV file
df.to_csv(feature_engineered_path, index=False)

print(f"Successfully engineered features and saved data to '{feature_engineered_path}'.")
print("\nFirst 5 rows of feature-engineered data:")
print(df.head())