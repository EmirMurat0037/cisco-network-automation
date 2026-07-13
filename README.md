# Cisco Network Automation & Infrastructure Management

This repository contains production-ready Python automation scripts designed to interact with Cisco network devices via RESTCONF and simulated environments. The project focuses on structured data parsing, robust exception handling, and automated network operations.

## 🚀 Features
* **Cisco Matrix Parser:** Robust JSON extraction mechanism with advanced `KeyError` handling for missing network parameters.
* **Network Alarm Center:** Real-time log monitoring and anomaly detection for core switch infrastructures.
* **Secure API Connection:** Base64 encrypted credentials handling for secure RESTCONF operations.
* **Fast Network Scanner:** Multi-threaded device health tracking and status verification.

## 🛠️ Tech Stack & Protocols
* **Language:** Python 3.x
* **Protocols:** RESTCONF / NETCONF
* **Data Formats:** JSON / YANG Data Models
* **Libraries:** `requests`, `json`, `base64`

## ⚙️ Robustness & Error Handling
Every script in this repository is built with a **defense-in-depth** programming approach:
* Prevents script failures during inventory loops using structural `try-except-else` blocks.
* Safe dictionary keys querying ensuring smooth automation even during missing device telemetries.