#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com

   Description:
   A script to interact with an "open" api,
   https://api.magicthegathering.io/v1/

   documentation for the API is available via,
   https://docs.magicthegathering.io/"""

# imports always go at the top of your code
import requests

# Define our "base" API
API = "https://api.magicthegathering.io/v1/" # this will never change regardless of the lookup we perform

def main():
    """Run time code"""

    set_code = input("What is the code of the set you are trying to lookup (see mtgsets.index for a list of codes)? ").lower()   # collect user input for MTG card set to lookup

    # create resp, which is our request object
    response = requests.get(f"{API}cards?set={set_code}")   # this "f" string reads: API + "cards/" + setcode

    # the .json() method will dump a JSON string into Pythonic data structures. COOL!
    # This is much easier than using the urllib.request library
    cards = response.json()

    print(cards)

if __name__ == "__main__":
    main()

