
# 🧠 MindFuel – Automated Daily Inspirational Quote Emailer

## 📌 Project Overview
This project is an automated email system designed to send daily inspirational quotes to active subscribers. It fetches a quote, retrieves subscriber information, sends personalized emails, and logs all delivery results for tracking and debugging.

## 🚀 Features

### ✔️ Daily Quote Extraction
Automatically fetches a motivational quote using the `extract_quote`
module.

### ✔️ Subscriber Fetching
Retrieves active subscribers from a database or data source via
`fetch_user`.

### ✔️ Personalized Email Sending
Sends each user a customized email containing their name and the daily
quote.

### ✔️ Retry Logic for Reliability
Each email is attempted **up to 3 times** before being marked as failed.

### ✔️ Logging System
All email activities are stored in: - logs/email_log.csv\
- logs/quote_fetched.txt

## 📂 Project Structure
    project-root/
    │
    ├── extract_quote.py
    ├── active_subscriber.py
    ├── send_email.py
    │
    └── logs/
        ├── email_log.csv
        └── quote_fetched.txt
    
## 🛠️ Tech Stack
- Python – scripting, automation
- SMTP / Gmail API – sending email
- ZenQuotes API – quote retrieval
- PostgreSQL – subscriber database
  
## ⚙️ How It Works
1.  Fetches a fresh quote and saves it.
2.  Retrieves subscriber list.
3.  Builds a personalized message for each user.
4.  Attempts to send email up to 3 times.
5.  Logs success or failure.

## 🚀 Running the Script
    python main.py
    
## 🛠️ Requirements
- Python 3.8+
- SMTP email configuration
- Modules used in:
  - extract_quote
  - fetch_user
  - send_email
  - 
## 🧑‍💻 Author
**Olusegun Olukayode**  
Data and Analytics Engineer | Business Intelligence Analyst | Automation Enthusiast

---
## 🎯 Purpose
_To inspire users daily through seamless email automation — combining simplicity, motivation, and reliability.

