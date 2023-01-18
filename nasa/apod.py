#!/usr/bin/env python3

import urllib.request
import json

## uncomment this import if you run in a GUI
## and want to open the URL in a browser
## import webbrowser

nasa_api = "https://api.nasa.gov/planetary/apod?"

def main():
    ## define credentials
    with open("/home/student/nasa.creds") as my_creds:
        nasa_creds = my_creds.read()

    ## remove "extra" new line feeds on our key
    nasa_creds = "api_key=" + nasa_creds.strip("\n")

    ## call the webservice
    apod_url_obj = urllib.request.urlopen(nasa_api + nasa_creds)

    ## read the file like object
    apod_read = apod_url_obj.read()
    
    ## decode the json file to python data structure
    apod = json.loads(apod_read.decode("utf-8"))

    ## display python data
    print("\n\nConverted Python Data")
    print(apod)

    print()

    print(apod["title"] + "\n")

    print(apod["date"] + "\n")

    print(apod["explanation"] + "\n")

    print(apod["url"])

    ## Uncomment the code below if running in a GUI
    ## and you want to open the URL in a browser
    ## use Firefox to open the HTTPS URL
    ## input("\nPress Enter to open NASA Picture of the Day in Firefox")
    ## webbrowser.open(decodeapod["url"])
if __name__ == "__main__":
    main()
