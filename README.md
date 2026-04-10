\# SOC Log Analysis \& Threat Detection Lab



\## Overview

This project simulates a Security Operations Center (SOC) environment by analyzing authentication logs to detect potential security threats such as brute-force attacks and suspicious login behavior.



\## Objective

\- Monitor login activity from log data

\- Detect brute-force attack patterns

\- Identify suspicious multi-user login attempts from a single IP

\- Generate structured security alerts



\## Technologies Used

\- Python

\- CSV (Log Data Simulation)



\## Features

\- Time-based brute-force attack detection

\- Severity classification (LOW, MEDIUM, HIGH)

\- Detection of multiple usernames attempted from a single IP

\- Structured alert output for security analysis



\## Sample Output

ALERT TYPE: Brute Force Attack  

IP Address: 192.168.1.10  

Failed Attempts: 6  

Severity: HIGH  



ALERT TYPE: Multiple Usernames Attempted  

IP Address: 192.168.1.10  

Usernames Tried: 3  

Severity: MEDIUM  



\## Learning Outcome

This project demonstrates practical SOC analyst skills including log monitoring, threat detection, and incident analysis using Python.



\## Future Improvements

\- Integration with real-time log sources

\- Visualization dashboard

\- Automated alert notifications

