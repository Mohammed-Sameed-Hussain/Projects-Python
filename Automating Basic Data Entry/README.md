# Real Estate Data Entry Automation (Zillow Clone)

This project is a Python-based automation tool that scrapes real estate property data from a Zillow-clone website and automatically fills out a Google Form with the retrieved information. This streamlined process allows for the easy collection of property addresses, prices, and links into a Google Sheet (via Google Forms).

## 🚀 Features

* **Web Scraping:** Uses `BeautifulSoup` to parse HTML and extract property details (Address, Price, Link) from a static real estate listing site.
* **Data Cleaning:** Implements `Regex` to clean price strings (removing monthly suffixes, symbols, etc.).
* **Form Automation:** Uses `Selenium Webdriver` to automatically fill and submit a Google Form for every property scraped.
* **Bilingual Support:** The Selenium script is designed to handle Google Form interface buttons in both **English** ("Submit") and **German** ("Senden").

## 🛠️ Built With

* [Python 3.x](https://www.python.org/)
* [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) - For parsing HTML and XML documents.
* [Requests](https://pypi.org/project/requests/) - For making HTTP requests to the target website.
* [Selenium](https://pypi.org/project/selenium/) - For browser automation and interaction.

## 📋 Prerequisites

Before running the script, ensure you have the following installed:

1.  **Python 3.x**
2.  **Chrome Browser**
3.  **Required Python Libraries:**

```bash
pip install beautifulsoup4 requests selenium
```


## ⚙️ How It Works

1. **Initialization:**
   * The script initializes the `Scrape` class.

2. **Scraping (`scrape_zwillio`):**
   * The script sends a request to the Zillow Clone website.
   * It parses the HTML to find all listing cards.
   * It extracts the listing link, the property address, and the price.
   * Regex is used to ensure the price is formatted correctly (e.g., `$1,200`).

3. **Data Entry (`fill_google_form`):**
   * A Chrome browser instance is launched using Selenium.
   * The script navigates to the specified Google Form.
   * It iterates through the list of scraped properties.
   * For each property, it fills in the inputs, clicks "Submit", and then selects "Submit another response" to continue the loop.

## ⚠️ Notes

* **Google Form Structure:** The script assumes the Google Form has 3 text input questions in this specific order:
    1. Address
    2. Price
    3. Property Link
    *If you change the form questions, you may need to adjust the `inputs` index in the code.*

* **Language Settings:** The script detects the "Submit" button using XPath logic that looks for either "Submit" or "Senden" (German), making it robust for users in DACH regions.

## 📄 License

Ha Ha. Nice Joke. This project is not worthy of license mate. :)
