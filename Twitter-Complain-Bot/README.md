# Internet Speed Complaint Bot 🚀

This is a Python automation script that monitors your internet speed and holds your ISP accounttable. It runs a speed test and, if the speeds are lower than what you were promised, automatically logs into Twitter (X) and posts a public complaint.

## 📋 Features

* **Automated Speed Testing:** Uses Selenium to navigate `speedtest.net` and initiate a test.
* **Robust Waiting Logic:** Intelligently waits for the test to finish by monitoring URL changes (instead of using hardcoded timers).
* **Persistent Profile:** Creates a local Chrome profile to store session data.
* **Auto-Complaint:** Checks results against your configured "Promised Speeds."
* **Twitter Automation:** Logs in and tweets a formatted message with your actual vs. promised speeds.
* **Language Support:** Includes XPath selectors for cookie banners in English and German (useful for users in Germany/EU).

## 🛠️ Prerequisites

* Python 3.x
* Google Chrome Browser
* **Selenium:** `pip install selenium`

## ⚙️ Configuration

Before running the script, open the Python file and update the constants at the top:

```python
PROMISED_UPLOAD = 35    # Your plan's upload speed (Mbps)
PROMISED_DOWNLOAD = 220 # Your plan's download speed (Mbps)
TWITTER_EMAIL = "your_email@example.com"
TWITTER_PASSWORD = "your_password"
