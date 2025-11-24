
class FlightData:
    """
    This class is responsible for structuring the flight data.
    It stores specific details about a flight such as price, origin, destination, and dates.
    """
    def __init__(self, departure_airport, destination_airport, price, departure_date, return_date):
        """
        Constructor to initialize the flight data object.
        """
        
        
        self._departure_airport_code = departure_airport
        self.price = price
        self.destination_airport = destination_airport
        self.departure_date = departure_date
        self.return_date = return_date
    
    def find_cheapest_flight(self, data) :
        """
        Parses the JSON response from the Amadeus API to find the cheapest flight option.
        
        Args:
            data (dict): The JSON response from the flight search API.
            
        Returns:
            FlightData: An object containing details of the cheapest flight found.
        """

        # Handle empty data or no flights found
        if data is None or not data['data']:
            print("No flight data")
            return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")
    
        # --- Initializing with the first flight ---
        first_flight = data['data'][0]
        lowest_price = float(first_flight["price"]["grandTotal"])
        origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
        destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
        out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
        return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]


        # Initialize FlightData with the first flight for comparison
        cheapest_flight = FlightData(origin, destination, lowest_price, out_date, return_date)

# --- Iterating through all available flights to find the lowest price ---
        for flight in data["data"]:
            price = float(flight["price"]["grandTotal"])
            
            # If we find a cheaper price, update the cheapest_flight object
            if price < lowest_price:
                lowest_price = price
                origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
                destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
                out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
                return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
                
                # Update the cheapest flight object
                cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)
                print(f"Lowest price to {destination} is £{lowest_price}")

        return cheapest_flight

    