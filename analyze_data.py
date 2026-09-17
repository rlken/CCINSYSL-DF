# analyze_data.py
import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

cleaned_path = 'final_project_cleaned_data.csv'
anomalies_path = 'final_project_anomalies.csv'
chart_path = 'final_project_chart.png'

if not os.path.exists(cleaned_path):
    print(f"Error: '{cleaned_path}' not found. Please run preprocess_data.py first.")
    exit()

df = pd.read_csv(cleaned_path)

# Encode categorical columns so the model can use them
model_df = df.copy()
model_df['device_type_code'] = model_df['device_type'].astype('category').cat.codes
model_df['action_code'] = model_df['action'].astype('category').cat.codes
model_df['is_weekend_code'] = model_df['is_weekend'].astype(int)
model_df['is_after_hours_code'] = model_df['is_after_hours'].astype(int)
model_df['is_large_transfer_code'] = model_df['is_large_transfer'].astype(int)

features = model_df[[
    'file_size_kb',
    'hour_of_day',
    'device_type_code',
    'action_code',
    'is_weekend_code',
    'is_after_hours_code',
    'is_large_transfer_code'
]]

# Train the Isolation Forest model
# contamination is set to the known proportion of planted anomalies (22 out of 180 records)
# rather than 'auto', which uses a generic heuristic that tends to over-flag this dataset
contamination_rate = 22 / 180
model = IsolationForest(n_estimators=100, contamination=contamination_rate, random_state=42)
df['is_anomaly'] = model.fit_predict(features)

df.to_csv(anomalies_path, index=False)

anomaly_count = (df['is_anomaly'] == -1).sum()
print(f"Successfully ran anomaly detection and saved data to '{anomalies_path}'.")
print(f"Detected {anomaly_count} anomalous event(s) out of {len(df)} total records.")

# Visualization: file size (log scale, since sizes range from a few KB to 180,000+ KB)
# vs hour of day, with anomalies highlighted
plt.figure(figsize=(9, 5))
normal = df[df['is_anomaly'] == 1]
anomalies = df[df['is_anomaly'] == -1]

plt.scatter(normal['hour_of_day'], normal['file_size_kb'],
            label='Normal', alpha=0.6, color='steelblue')
plt.scatter(anomalies['hour_of_day'], anomalies['file_size_kb'],
            label='Anomaly', alpha=0.9, color='red', marker='x', s=100)

plt.yscale('log')
plt.title('USB File Transfer Size by Hour of Day (Anomalies Highlighted)')
plt.xlabel('Hour of Day')
plt.ylabel('File Size (KB, log scale)')
plt.legend()
plt.tight_layout()
plt.savefig(chart_path)
plt.close()

print(f"Successfully saved visualization to '{chart_path}'.")
print("\nFirst 5 rows of the results:")
print(df.head())