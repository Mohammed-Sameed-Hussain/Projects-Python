✈️ Flight Deal Finder

A Python-based automation tool that tracks flight prices for your favorite destinations and sends instant alerts (via SMS or WhatsApp) when a deal is found below your target price.

This project was built to automate the process of finding cheap flights, specifically configured to track flights departing from Munich (MUC), but easily customizable for any origin city.

🌟 Features

Google Sheets Integration: Automatically reads destination cities and target prices from a Google Sheet using the Sheety API.

IATA Code Auto-Fill: If your Google Sheet only has city names, the tool automatically finds the correct IATA airport codes (e.g., "Paris" -> "PAR") and updates the sheet.

Real-time Flight Search: Uses the Amadeus API to search for the cheapest flights for the next 6 months.

Smart Alerts: Compares real-time prices with your target "lowest price." If a deal is found, it sends a notification via Twilio.

Multi-Channel Notifications: Supports both SMS and WhatsApp alerts.

🛠️ Tech Stack

Language: Python 3.x

APIs Used:

Amadeus (Flight Search)

Sheety (Google Sheets as a Database)

Twilio (SMS & WhatsApp Messaging)

Libraries: requests, twilio, python-dotenv

📂 Project Structure

main.py: The entry point. It orchestrates the flow between data fetching, searching, and notifying.

data_manager.py: Handles communication with the Google Sheet (getting data and updating IATA codes).

flight_search.py: Interfaces with the Amadeus API to find airport codes and search for flight offers.

flight_data.py: Structures the flight data and contains logic to find the cheapest flight from the JSON response.

notification_manager.py: Handles sending messages via the Twilio API.

🚀 Setup & Installation

Clone the repository

git clone [https://github.com/yourusername/flight-deal-finder.git](https://github.com/yourusername/flight-deal-finder.git)
cd flight-deal-finder


Install dependencies

pip install requests twilio python-dotenv


Configure Environment Variables
Create a .env file in the root directory. You will need API keys from Amadeus, Sheety, and Twilio. Add them to the file as shown below:

# Amadeus API Keys
AMADEUS_API_KEY=your_amadeus_api_key
AMADEUS_SECRECT=your_amadeus_api_secret

# Sheety Authentication
SHEETY_USRERNAME=your_sheety_username
SHEETY_PASSWORD=your_sheety_password

# Twilio Configuration
TWILIO_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_VIRTUAL_NUMBER=your_twilio_phone_number
TWILIO_VERIFIED_NUMBER=your_personal_phone_number
TWILIO_WHATSAPP_NUMBER=your_twilio_whatsapp_number


Note: Ensure the variable names match exactly as above (including spellings) to align with the Python code.

Google Sheet Setup

Create a Google Sheet with columns: City, IATA Code, Lowest Price.

Connect it to Sheety.

Enable GET and PUT requests in your Sheety project settings.

▶️ Usage

Run the main script:

python main.py


The script will first check your Google Sheet.

If IATA Code is missing for any city, it will fetch it and update the sheet.

It will then search for flights from Munich (MUC) (configurable in main.py) to all destinations in your sheet.

If a flight is found cheaper than your Lowest Price, you will receive a WhatsApp/SMS alert!

