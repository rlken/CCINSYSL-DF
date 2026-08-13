# entity_extractor.py
import pandas as pd
import os
import spacy

anomalies_path = 'anomalies_detected_evidence.csv'
entities_path = 'extracted_entities.csv'

if not os.path.exists(anomalies_path):
    print(f"Error: '{anomalies_path}' not found. Please complete Week 4 activity first.")
    exit()

# Load the pre-trained SpaCy English language model
nlp = spacy.load('en_core_web_sm')

df = pd.read_csv(anomalies_path)

# Collect all named entities found across every message
extracted_rows = []
for idx, row in df.iterrows():
    message = row.get('message', '')
    if pd.isna(message):
        continue
    doc = nlp(str(message))
    for ent in doc.ents:
        extracted_rows.append({
            'record_index': idx,
            'message': message,
            'entity_text': ent.text,
            'entity_label': ent.label_
        })

entities_df = pd.DataFrame(extracted_rows)
entities_df.to_csv(entities_path, index=False)

print(f"Successfully extracted entities and saved data to '{entities_path}'.")
print(f"Found {len(entities_df)} entities across {len(df)} records.")
print("\nFirst 5 rows of extracted entities:")
print(entities_df.head())