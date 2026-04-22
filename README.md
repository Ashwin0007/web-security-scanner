# Web Security Scanner 🔐

A Python-based web security scanner that identifies missing security headers and common misconfigurations.

## Features
- Checks critical HTTP security headers
- Assigns severity levels (HIGH / MEDIUM / LOW)
- Provides risk explanations
- Detects HTTPS usage
- Identifies server information leakage
- Generates a detailed report file

## Installation

```bash
pip install -r requirements.txt
```

Usage
```bash
python scanner.py https://example.com
```

Output:

```
[HIGH] Missing Content-Security-Policy → Risk: Prevents XSS attacks
[OK] X-Frame-Options is present
[MEDIUM] Site is not using HTTPS
[LOW] Server header exposed: nginx
```

Output Report

The tool generates a report file:

```
report_example.com.txt
```

## Security Insights
Missing Content-Security-Policy (CSP) can lead to Cross-Site Scripting (XSS)

Missing X-Frame-Options can lead to Clickjacking attacks

Lack of HTTPS exposes users to Man-in-the-Middle attacks

## Why I Built This

This project simulates basic Dynamic Application Security Testing (DAST) techniques and demonstrates how automated tools can identify common web security misconfigurations.

## ⚠️ Disclaimer

This tool is intended for educational purposes only.

DO NOT USE this tool on websites without proper authorization.

Unauthorized scanning of systems may be illegal and could result in legal consequences.

The author is not responsible for any misuse of this tool.

## ⚠️ Example 

USAGE

<img width="1126" height="396" alt="image" src="https://github.com/user-attachments/assets/448ec73c-e7ac-4af3-bc36-dc934a63d19a" />
</br>

REPORT

<img width="1212" height="362" alt="image" src="https://github.com/user-attachments/assets/cd117360-40e2-4bbd-b2ec-8c2473cc63f0" />

