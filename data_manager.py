import requests
from pprint import pprint

SHEETY_PRICES_ENDPOINT = 'https://api.sheety.co/ff1183adec43520d59ee2ddd3b4c7588/copyOfFlightDeals/prices'




class DataManager:

    def __init__(self):
        self.destination_data = {}

    def destination_data(self):
        #step 2 getting the Sheety API to GET all the data in that sheet and print it out
        response = requests.get(SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data ["prices"]
        #step 3 Importing pretty print and printing data out again using pprint() to see if it formatted
        #pprint(data)
        return self.destination_data