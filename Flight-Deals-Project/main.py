# This file serves as the main entry point. It orchestrates the DataManager, 
# FlightSearch, FlightData, and NotificationManager classes.


import time
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager


# --- 1. Set up the Data Manager and fetch current Google Sheet data ---
data_manager  = DataManager()
sheet_data = data_manager.get_sheet_data()

# --- 2. Set up Search and Notification Managers ---
flight_search = FlightSearch()
notification_manager = NotificationManager()


# Origin Airport (Munich)

ORIGIN_CITY_IATA = "MUC"

# --- 3. Check if Sheet has missing IATA Codes ---
# If the first row is empty, we assume we need to fill the sheet.

if sheet_data[0].get("iataCode", "") == "" :
    from flight_search import FlightSearch
    
    flight_iata_search = FlightSearch()

    for row in sheet_data:
        # Fetch IATA code for the city name in the row
        row['iataCode'] = flight_iata_search.get_destination_code(row['city'])
    
    print(f"sheet_data:\n {sheet_data}")

    data_manager.sheet_data = sheet_data
    data_manager.update_sheet_data()



# --- 4. Search for Flights ---


tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination}")

    # Search for flights from Origin to Destination
    flights = flight_search.get_flight_deals(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    # Analyze the results to find the cheapest one
    cheapest_flight = find_cheapest_flight(flights)


    # --- 5. Check against the Price Limit and Notify ---
    # If valid flight found AND price is lower than the 'lowestPrice' in our Google Sheet

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        print(f"Lower price flight found to {destination['city']}!")
        # notification_manager.send_sms(
        #     message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
        #                  f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
        #                  f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        # )
        
        notification_manager.send_whatsapp(
            message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
                         f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                         f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )



