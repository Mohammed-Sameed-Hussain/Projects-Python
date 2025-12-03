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

### Option 1: GitHub Actions (Recommended for Free Scheduling)

GitHub Actions allows you to run this script on a schedule for free.

1. Push your code to a GitHub repository.
2. Add your `MY_EMAIL` and `MY_PASSWORD` to the repository's **Settings > Secrets and variables > Actions**.
3. Create a file at `.github/workflows/scrape.yml` with the following content to run it every 6 hours:

```yaml
name: Check Price
on:
  schedule:
    - cron: '0 */6 * * *'  # Runs every 6 hours
  workflow_dispatch:       # Allows manual run

jobs:
  scrape:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          pip install requests beautifulsoup4 python-dotenv
      - name: Run script
        env:
          MY_EMAIL: ${{ secrets.MY_EMAIL }}
          MY_PASSWORD: ${{ secrets.MY_PASSWORD }}
        run: python main.py
```
### Option 2: PythonAnywhere

[PythonAnywhere](https://www.pythonanywhere.com) is a beginner-friendly platform that lets you upload your script and run it.

1. Create a free account on PythonAnywhere.
2. Upload your `main.py`, `amazon_scrape.py`, and `email_notificaiton.py` files to the "Files" tab.
3. Go to the **Tasks** tab.
4. Set the time (UTC) you want it to run.
5. Enter the command: `python3.10 /home/yourusername/main.py` *(Note: The free tier usually allows 1 daily scheduled task. For more frequent checks, a small paid plan or GitHub Actions is better.)*

## 📂 Project Structure
- `main.py`: The entry point. It orchestrates the scraping and notification logic.
- `amazon_scrape.py` : Handles the connection to Amazon, HTML parsing, and data extraction.
- `email_notificaiton.py` : Manages the SMTP connection and email composition.

## 🇩🇪 Localization Notes
- **Region**: The code is optimized for Amazon Germany (amazon.de).

- **Currency**: It specifically looks for the Euro symbol (`€`) , which is standard in Germany.


## ⚠️ Disclaimer
Web scraping may violate Amazon's Terms of Service. This script is intended for educational purposes and personal use only. Use responsibly and avoid sending excessive requests to the server.
