#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_char_lookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        got_response = requests.get(AOIF_CHAR + got_char_lookup)

        ## Decode the response
        got_decoded = got_response.json()
        pprint.pprint(got_decoded)
        
        houses = []
        for house in got_decoded["allegiances"]:
            house_response = requests.get(house)
            house_decoded = house_response.json()
            houses.append(house_decoded["name"])
        print(houses)

if __name__ == "__main__":
        main()
