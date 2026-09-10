"""
Week 11 - Final Project: Data Acquisition
Generates a simulated raw evidence file: USB / file transfer logs.

Produces: final_project_raw_data.csv
"""

import csv
import random
from datetime import datetime, timedelta

random.seed(42)  # reproducible output

USERS = [f"EMP{n}" for n in (1001, 1042, 1077, 1103, 1150, 1188, 1204, 1233)]
HOSTS = [f"WORKSTATION-{n:02d}" for n in range(1, 9)]
DEVICE_TYPES = ["USB Flash Drive", "External HDD", "Smartphone", "SD Card"]
ACTIONS = ["CONNECT", "DISCONNECT", "COPY", "DELETE", "RENAME"]

NORMAL_FILES = [
    "meeting_notes.docx", "weekly_report.xlsx", "presentation.pptx",
    "photo.jpg", "backup.zip", "notes.txt", "invoice.pdf", "schedule.xlsx",
]
SENSITIVE_FILES = [
    "confidential_report.pdf", "salary_data.xlsx", "client_database.csv",
    "passwords.txt", "merger_agreement.docx", "source_code.zip",
]

START = datetime(2026, 8, 1, 0, 0, 0)
ROWS = 180
ANOMALY_ROWS = 12  # planted suspicious after-hours large transfers


def random_device_id():
    return "USB-" + "".join(random.choices("0123456789ABCDEF", k=8))


def normal_row(i):
    ts = START + timedelta(
        days=random.randint(0, 20),
        hours=random.choice(range(8, 19)),  # normal business hours
        minutes=random.randint(0, 59),
    )
    action = random.choice(ACTIONS)
    file_name = random.choice(NORMAL_FILES)
    file_size = round(random.uniform(20, 5000), 1)

    # simulate occasional messy/missing data
    ts_str = ts.strftime("%Y-%m-%d %H:%M:%S")
    if random.random() < 0.05:
        ts_str = ts.strftime("%m/%d/%Y %H:%M")  # inconsistent format
    if random.random() < 0.08:
        file_size = ""  # missing value

    return {
        "timestamp": ts_str,
        "user_id": random.choice(USERS),
        "host_computer": random.choice(HOSTS),
        "device_id": random_device_id(),
        "device_type": random.choice(DEVICE_TYPES),
        "action": action,
        "file_name": file_name,
        "file_size_kb": file_size,
    }


def anomalous_row(i):
    # after-hours, unusually large transfer of a sensitive file
    ts = START + timedelta(
        days=random.randint(0, 20),
        hours=random.choice([0, 1, 2, 3, 22, 23]),
        minutes=random.randint(0, 59),
    )
    return {
        "timestamp": ts.strftime("%Y-%m-%d %H:%M:%S"),
        "user_id": random.choice(USERS),
        "host_computer": random.choice(HOSTS),
        "device_id": random_device_id(),
        "device_type": random.choice(["USB Flash Drive", "External HDD"]),
        "action": "COPY",
        "file_name": random.choice(SENSITIVE_FILES),
        "file_size_kb": round(random.uniform(50000, 200000), 1),
    }


def main():
    rows = [normal_row(i) for i in range(ROWS - ANOMALY_ROWS)]
    rows += [anomalous_row(i) for i in range(ANOMALY_ROWS)]
    random.shuffle(rows)

    fieldnames = [
        "timestamp", "user_id", "host_computer", "device_id",
        "device_type", "action", "file_name", "file_size_kb",
    ]

    with open("final_project_raw_data.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Generated final_project_raw_data.csv with {len(rows)} rows.")


if __name__ == "__main__":
    main()
