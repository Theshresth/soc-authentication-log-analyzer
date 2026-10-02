import re
from collections import Counter

LOG_FILE = "/var/log/auth.log"
THRESHOLD = 5

failed_attempts = []

with open(LOG_FILE, "r", errors="ignore") as log:
    for line in log:
        if "Failed password" not in line:
            continue

        match = re.search(
            r"Failed password for (?:invalid user )?(\S+) from (\S+)",
            line
        )

        if match:
            username = match.group(1)
            source_ip = match.group(2)
            failed_attempts.append((username, source_ip))

ip_counts = Counter(ip for username, ip in failed_attempts)
user_counts = Counter(username for username, ip in failed_attempts)

print("=== SOC Authentication Log Analyzer ===")
print(f"Total failed SSH attempts: {len(failed_attempts)}")

print("\nFailed attempts by source IP:")
for ip, count in ip_counts.items():
    status = "ALERT" if count >= THRESHOLD else "Normal"
    print(f"{ip}: {count} attempts -> {status}")

print("\nFailed attempts by username:")
for username, count in user_counts.items():
    print(f"{username}: {count} attempts")
