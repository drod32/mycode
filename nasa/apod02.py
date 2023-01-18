#!/usr/bin/env python3

import requests

nasa_api = "https://api.nasa.gov/planetary/apod?"

def return_creds():
    ## grab credentials from local file
    with open("/home/student/nasa.creds", "r") as my_creds:
        nasa_creds = my_creds.read()

    ## remove newline characters from api key
    nasa_creds = "api_key=" + nasa_creds.strip("\n")
    return nasa_creds

## this is the main function
def main():
    ## grab credentials
    nasa_creds = return_creds()

    ## call apod api
    apod_response = requests.get(nasa_api + nasa_creds)

    ## strip off json
    apod = apod_response.json()

    print(apod)

    print()

    print(apod["title"] + "\n")

    print(apod["date"] + "\n")

    print(apod["explanation"])

    print(apod["url"])

if __name__ == "__main__":
    main()

