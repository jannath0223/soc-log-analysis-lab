import csv
from collections import defaultdict
from datetime import datetime

failed_attempts = defaultdict(list)
user_activity = defaultdict(set)

# ✅ Single pass (efficient)
with open('../logs/auth_logs.csv', 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        ip = row['ip']
        user = row['username']
        status = row['status']
        time = datetime.strptime(row['timestamp'], "%Y-%m-%d %H:%M")

        # Track failed attempts
        if status == 'failed':
            failed_attempts[ip].append(time)

        # Track users per IP
        user_activity[ip].add(user)

print("=== SOC Threat Detection Report ===\n")

# 🔥 Brute force & suspicious detection
for ip, times in failed_attempts.items():
    times.sort()
    count = len(times)

    # Severity logic
    if count >= 4:
        severity = "HIGH"
    elif count == 3:
        severity = "MEDIUM"
    elif count == 2:
        severity = "LOW"
    else:
        continue

    # Time-based detection
    brute_force = False
    for i in range(len(times) - 2):
        diff = (times[i+2] - times[i]).total_seconds() / 60
        if diff <= 5:
            brute_force = True
            break

    print(f"ALERT TYPE: {'Brute Force Attack' if brute_force else 'Suspicious Activity'}")
    print(f"IP Address: {ip}")
    print(f"Failed Attempts: {count}")
    print(f"Severity: {severity}")
    print("-" * 40)

print("\n=== Additional Threat Detection ===\n")

# 🔥 Multi-user attack detection
for ip, users in user_activity.items():
    if len(users) > 2:
        print("ALERT TYPE: Multiple Usernames Attempted")
        print(f"IP Address: {ip}")
        print(f"Usernames Tried: {len(users)}")
        print("Severity: MEDIUM")
        print("-" * 40)