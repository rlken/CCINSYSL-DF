# Final Project Forensic Report: USB Device Data Exfiltration Investigation

## Executive Summary
This investigation analyzed 180 simulated USB device activity logs across eight monitored workstations to
identify potential insider data exfiltration. Using an Isolation Forest anomaly detection model applied to
file size, hour of day, device type, action type, and after-hours/large-transfer flags, 22 events were flagged
as anomalous. These flagged events were overwhelmingly characterized by unusually large file transfers
(70,000 KB and above) occurring between midnight and 4 AM, well outside normal business hours, and
frequently involved sensitive file types such as salary records, client databases, and confidential reports.
This pattern is consistent with a deliberate, after hours data exfiltration attempt rather than routine
employee activity.

## Methodology
1. **Data Acquisition:** A simulated dataset of 180 USB device activity logs was generated, capturing
   `timestamp`, `user_id`, `host_computer`, `device_id`, `device_type` (USB Flash Drive, External HDD, SD
   Card, Smartphone), `action` (COPY, DELETE, CONNECT, DISCONNECT, RENAME), `file_name`, and
   `file_size_kb` for each event.
2. **Preprocessing:** Missing file sizes were filled using the median value, timestamps were converted to
   proper datetime objects, and additional features were engineered: `hour_of_day`, `is_weekend`,
   `is_after_hours`, `file_extension`, and `is_large_transfer`.
3. **Analysis:** An Isolation Forest model — an unsupervised anomaly detection algorithm — was trained on
   file size, hour of day, device type, action type, weekend flag, after hours flag, and large-transfer flag to
   identify events that deviated significantly from normal USB usage patterns.
4. **Visualization:** A scatter plot was generated showing file size (log scale) against hour of day, with
   anomalous events highlighted in red, to visually distinguish suspicious large, after-hours transfers from
   routine daytime USB activity.

## Key Findings
- **Total events analyzed:** 180 simulated USB transfer logs
- **Anomalous events detected:** 22
- **Deliberately planted anomalies in the simulated data:** 22 (large, after-hours transfers)
- The model's detection count matched the planted anomaly count exactly, with no false positives observed
  among the sampled normal records. The flagged anomalies were concentrated in the early morning hours
  (roughly midnight to 4 AM) and involved file sizes well above 70,000 KB — far exceeding the typical
  transfer size of a few thousand KB seen in normal daytime activity. The flagged transfers frequently
  involved sensitive file types such as `salary_data.xlsx`, `client_database.csv`, `confidential_report.pdf`,
  and `merger_agreement.docx`, most often copied to USB Flash Drives or External HDDs.

![USB Transfer Anomalies](final_project_chart.png)

*Figure: File size (KB, log scale) by hour of day for USB device activity. Anomalous events, flagged by the
Isolation Forest model, are shown in red.*

## Conclusion
The flagged events represent a clear and consistent deviation from typical USB usage across the monitored
workstations, with the model's 22 detected anomalies aligning exactly with the anomalies planted in the
simulated dataset. This suggests that combining file size, time of day, and transfer-behavior features with
an Isolation Forest model is an effective approach for surfacing suspicious USB activity without requiring
prior labeled examples of "malicious" behavior. In a real investigation, these findings would warrant further
manual review, particularly of the specific user IDs and host computers associated with these large,
after-hours transfers of sensitive files. Recommended next steps include restricting USB write access for
sensitive file types outside of business hours, enabling real-time alerting for large transfers matching this
pattern, and cross-referencing the flagged user IDs against physical access logs to corroborate whether the
employee was on-site at the time of the transfer.

## References
- Pandas (data manipulation)
- Scikit-learn — IsolationForest (unsupervised anomaly detection)
- Matplotlib (data visualization)