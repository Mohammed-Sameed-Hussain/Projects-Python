# Amazon Price Tracker 📉
A Python-based automation tool that monitors product prices on Amazon.de and sends an email notification when the price drops below a specified threshold.


## 📌 Overview
This project was built to track the price of specific items (currently configured for a Fujifilm X-T50 camera) on Amazon Germany. It scrapes the live product page, parses the Euro pricing, and triggers an SMTP email alert if the current price is lower than your target buy price.


## 🚀 Features

- **Web Scraping:** Uses `BeautifulSoup` and `requests` to fetch real-time data from Amazon.
- **Price Parsing:** specifically handles European currency formatting (e.g., stripping `€` symbols and handling comma decimals).
- **Email Alerts:** Uses `smtplib` to send automated alerts via Gmail.
- **Security:** Uses environment variables to keep email credentials safe.


## 🛠️ Prerequisites

- Python 3.x
- A Gmail account (with an App Password enabled for SMTP access).


## 📦 Installation

1. **Clone the repository** (or download the files):
```bash
git clone [https://github.com/yourusername/amazon-price-tracker.git](https://github.com/yourusername/amazon-price-tracker.git)
cd amazon-price-tracker
```
2. **Install required packages**: You will need `requests`, `beautifulsoup4`, and `python-dotenv`.
```bash
pip install requests beautifulsoup4 python-dotenv
```


## ⚙️ Configuration

1. **Environment Variables**
For security, this project uses a `.env` file to store credentials. Create a file named `.env` in the same directory as `main.py` and add the following:
```env
MY_EMAIL="your_email@gmail.com"
MY_PASSWORD="your_google_app_password"
```
    
**Note**: Do not use your standard Gmail login password. You must generate a specific **App Password** in your Google Account settings under *Security > 2-Step Verification > App passwords*.

2. **Adjusting the Target Product**
To track a different product, modify `amazon_scrape.py`:
- Update `self.live_url` with the new Amazon product link.
- **Important**: Ensure the new link is from the same region (Amazon.de) or adjust the currency parsing logic in `get_price_title()` if switching to a region that uses `.` for decimals (like the US).

3. **Setting the Buy Price**
Open `main.py` and update the `BUY_PRICE` constant:
```env
BUY_PRICE = 1100  # Set your target price in Euros
```

## ▶️ Usage
Run the main script to check the price:
```bash
python main.py
```
If the price is below your threshold, you will receive an email immediately. If not, the script will finish without sending an alert.


## ☁️ Deployment / Automation

To run this script automatically (e.g., a few times a day for a month) without keeping your computer on, you can deploy it to a cloud server.


## 📂 Project Structure
- `main.py`: The entry point. It orchestrates the scraping and notification logic.
- `amazon_scrape.py` : Handles the connection to Amazon, HTML parsing, and data extraction.
- `email_notificaiton.py` : Manages the SMTP connection and email composition.

## 🇩🇪 Localization Notes
- **Region**: The code is optimized for Amazon Germany (amazon.de).

- **Currency**: It specifically looks for the Euro symbol (`€`) , which is standard in Germany.


## ⚠️ Disclaimer
Web scraping may violate Amazon's Terms of Service. This script is intended for educational purposes and personal use only. Use responsibly and avoid sending excessive requests to the server.
