# SOC Authentication Log Analyzer

A Python-based SOC lab project for analyzing Linux authentication logs and detecting repeated failed SSH authentication attempts.

## Objective

Build a lightweight authentication-log analyzer that can:

- Parse `/var/log/auth.log`
- Detect failed SSH authentication attempts
- Aggregate attempts by source IP
- Aggregate attempts by username
- Generate threshold-based alerts
- Support basic SOC-style investigation

## Environment

- Ubuntu Linux
- Python 3
- Linux CLI
- `/var/log/auth.log`

## Investigation Workflow

1. Collect authentication events from `/var/log/auth.log`
2. Investigate failed authentication events using `grep`
3. Identify source IP addresses and usernames
4. Process the log using Python
5. Count failed attempts
6. Apply a detection threshold
7. Investigate the alert context
8. Determine whether the activity is suspicious or benign

## Detection Logic

The analyzer uses a threshold of 5 failed SSH authentication attempts from the same source IP.

If the number of attempts is greater than or equal to the threshold, the script generates an `ALERT`.

## Sample Lab Finding

The analyzer detected:

- Total failed SSH attempts: 6
- Source IP: `127.0.0.1`
- Failed attempts from source: 6
- Username `shresthsoni`: 3 attempts

The source IP `127.0.0.1` represents the local Ubuntu system.

## Investigation Result

The threshold rule generated an alert because 6 failed SSH attempts exceeded the configured threshold of 5.

However, the source was `127.0.0.1` (localhost). Therefore, the evidence from this controlled lab does not establish an external brute-force attack.

The activity was classified as local/controlled authentication activity.

## Skills Demonstrated

- Linux authentication-log analysis
- SSH log investigation
- `grep`
- Python log parsing
- Regular expressions
- Source IP aggregation
- Username aggregation
- Threshold-based detection
- Basic SOC alert analysis
- Evidence-based incident assessment

## Disclaimer

This project was performed in a controlled Ubuntu virtual-machine environment for cybersecurity learning and SOC analyst practice.
