# final_report.py
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

anomalies_path = 'anomalies_detected_evidence.csv'
entities_path = 'extracted_entities.csv'
image_path = 'event_distribution.png'
report_path = 'forensic_report.md'

if not os.path.exists(anomalies_path):
    print(f"Error: '{anomalies_path}' not found. Please complete Week 4 activity first.")
    exit()
if not os.path.exists(entities_path):
    print(f"Error: '{entities_path}' not found. Please complete Week 5 activity first.")
    exit()

df_anomalies = pd.read_csv(anomalies_path)
df_entities = pd.read_csv(entities_path)

total_events = len(df_anomalies)
anomaly_count = (df_anomalies['is_anomaly'] == -1).sum()
entity_count = len(df_entities)

# Visualization: bar chart of event type counts
event_counts = df_anomalies['event_type'].value_counts()
plt.figure(figsize=(8, 5))
event_counts.plot(kind='bar', color='steelblue')
plt.title('Distribution of Event Types')
plt.xlabel('Event Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig(image_path)
plt.close()

# Entity label breakdown
entity_label_counts = df_entities['entity_label'].value_counts()

# Build the markdown report
report_lines = []
report_lines.append("# Forensic Investigation Report\n")
report_lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

report_lines.append("## Executive Summary\n")
report_lines.append(
    f"This report summarizes the findings of an automated forensic analysis conducted on a simulated "
    f"digital evidence dataset. A total of {total_events} events were analyzed, of which {anomaly_count} "
    f"were flagged as anomalous by an unsupervised machine learning model. Additionally, {entity_count} "
    f"named entities were extracted from message content, providing potential investigative leads.\n"
)

report_lines.append("## Methodology\n")
report_lines.append(
    "The investigation followed a structured pipeline: raw event data was acquired and cleaned, "
    "new time-based features (hour of day, day of week, weekend flag) were engineered, an Isolation "
    "Forest model was applied to detect anomalous behavior, and a Named Entity Recognition (NER) model "
    "(SpaCy) was used to extract people, organizations, and locations from message text.\n"
)

report_lines.append("## Key Findings\n")
report_lines.append(f"- **Total events analyzed:** {total_events}")
report_lines.append(f"- **Anomalous events detected:** {anomaly_count}")
report_lines.append(f"- **Named entities extracted:** {entity_count}\n")

report_lines.append("### Entity Breakdown\n")
for label, count in entity_label_counts.items():
    report_lines.append(f"- **{label}:** {count}")
report_lines.append("")

report_lines.append("## Event Distribution Visualization\n")
report_lines.append(f"![Event Distribution]({image_path})\n")

with open(report_path, 'w') as f:
    f.write("\n".join(report_lines))

print(f"Successfully generated visualization '{image_path}' and report '{report_path}'.")