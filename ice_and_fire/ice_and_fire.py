#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests

AOIF = "https://www.anapioficeandfire.com/api"

def main():
    ## Send HTTPS GET to the API of ICE and Fire
    got_response = requests.get(AOIF)

    ## Decode the response
    got_decoded = got_response.json()

    ## print the response
    print(got_decoded)
    
    ## display only the keys within
    ## the dictionary by using dict.keys()
    ## great for seeing what keys are available for lookup
    print(got_decoded.keys())
    

if __name__ == "__main__":
    main()


