
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
AMADEUS_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_DEAL_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"

import requests
from datetime import datetime
import os
from dotenv import load_dotenv

class FlightSearch:
    """
    This class is responsible for talking to the Amadeus Flight Search API.
    It handles authentication (OAuth2) and searching for cities and flights.
    """

    def __init__(self):
        """
        Initialize with API credentials and immediately fetch a session token.
        """

        self._api_key = os.environ["AMADEUS_API_KEY"]
        self._api_secret = os.environ["AMADEUS_SECRECT"]
        self._token = self._get_new_token()
    

    def _get_new_token(self):
        """
        Generates a new OAuth2 access token from Amadeus.
        The token is required for all subsequent API calls.
        """


        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }

        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']
    




    def get_destination_code(self, city_name):
        """
        Retrieves the IATA code (e.g., 'LHR', 'JFK') for a given city name.
        
        Args:
            city_name (str): The name of the city (e.g., 'Paris').
        Returns:
            str: The IATA code, or 'N/A' / 'Not Found' if unsuccessful.
        """


        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(url=AMADEUS_ENDPOINT,headers=headers,params=query)
        
        
        print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code


    def get_flight_deals(self,departure_city_code, destination_city_code, start_date, end_date):
        """
        Searches for flight offers between two cities for specific dates.
        """

        
        headers = {"Authorization": f"Bearer {self._token}"} 

        query = {
            "originLocationCode" : departure_city_code,
            "destinationLocationCode" : destination_city_code,
            "departureDate" : start_date.strftime(f"%Y-%m-%d"),
            "returnDate" : end_date.strftime(f"%Y-%m-%d"),
            "adults" : 1,
            "currencyCode" : "EUR",
            "max" : "10"
        }  

        response = requests.get(url=FLIGHT_DEAL_ENDPOINT,headers=headers,params=query)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()




# flight_search = FlightSearch()



