# anomaly_detector.py
import pandas as pd
import os
from sklearn.ensemble import IsolationForest

feature_data_path = 'feature_engineered_evidence.csv'
anomalies_path = 'anomalies_detected_evidence.csv'

if not os.path.exists(feature_data_path):
    print(f"Error: '{feature_data_path}' not found. Please complete Week 3 activity first.")
    exit()

df = pd.read_csv(feature_data_path)

# Select the engineered features to base anomaly detection on
# We convert categorical columns (event_type, day_of_week) into numbers the model can use
model_df = df.copy()
model_df['event_type_code'] = model_df['event_type'].astype('category').cat.codes
model_df['day_of_week_code'] = model_df['day_of_week'].astype('category').cat.codes
model_df['is_weekend_code'] = model_df['is_weekend'].astype(int)

features = model_df[['hour_of_day', 'event_type_code', 'day_of_week_code', 'is_weekend_code']]

# Train the Isolation Forest model
# contamination='auto' lets the model estimate the proportion of anomalies itself
model = IsolationForest(n_estimators=100, contamination='auto', random_state=42)
df['is_anomaly'] = model.fit_predict(features)

# is_anomaly will be -1 for anomalies and 1 for normal points
df.to_csv(anomalies_path, index=False)

anomaly_count = (df['is_anomaly'] == -1).sum()
print(f"Successfully ran anomaly detection and saved data to '{anomalies_path}'.")
print(f"Detected {anomaly_count} anomalous event(s) out of {len(df)} total records.")
print("\nFirst 5 rows of the results:")
print(df.head())