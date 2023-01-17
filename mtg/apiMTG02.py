#!/usr/bin/env python3

"""Alta3 Research | Author: RZFeeser@alta3.com

   Description:
   A script to interact with an "open" api,
   https://api.magicthegathering.io/v1/

   documentation for the API is available via,
   https://docs.magicthegathering.io/"""

# always import at top of page
import requests

# define "base" api

api = "https://api.magicthegathering.io/v1/"

def main():
    """runtime-code"""

    # create response, which is request object
    response = requests.get(f"{api}sets")

    # display the methods available to our new object
    print( dir(response) )

if __name__ == "__main__":
    main()


