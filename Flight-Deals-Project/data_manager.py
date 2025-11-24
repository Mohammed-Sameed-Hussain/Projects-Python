import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Sheety API Endpoints
sheety_GET_API = "https://api.sheety.co/1f82896a66c8fabd9e849524d5071bf1/flightDeals/prices"

## https://api.sheety.co/1f82896a66c8fabd9e849524d5071bf1/flightDeals/prices/[Object ID]
sheety_PUT_API = 'https://api.sheety.co/1f82896a66c8fabd9e849524d5071bf1/flightDeals/prices/'









class DataManager:
    """
    This class is responsible for talking to the Google Sheet via the Sheety API.
    It handles getting the city data and updating the IATA codes.
    """
    def __init__(self):
        """
        Initialize with Sheety credentials from environment variables.
        """
        self._user = os.environ["SHEETY_USRERNAME"]
        self._password = os.environ["SHEETY_PASSWORD"]
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.sheet_data = {}
        pass

    
    def get_sheet_data(self):
        """
        Fetches the current data from the Google Sheet.
        Returns:
            list: A list of dictionaries representing the rows in the sheet.
        """
        response_sheet = requests.get(url=sheety_GET_API,auth=self._authorization)
        data = response_sheet.json()
        print(data)
        self.sheet_data = data['prices']
        return self.sheet_data
        # print(self.sheet_data)

    def update_sheet_data(self):
        """
        Iterates over the local sheet_data and updates the IATA codes in the Google Sheet 
        using a PUT request.
        """
        
        for city in self.sheet_data:
            new_data_entry = {
                "price" : {
                    'iataCode' : city['iataCode'] 
                }
            }
        
            response = requests.put(url=f"{sheety_PUT_API}/{city['id']}", auth=self._authorization, json=new_data_entry)
        
            print(response.text)

