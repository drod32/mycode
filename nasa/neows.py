#!/usr/bin/python3
import requests

## Define NEOW URL
neo_url = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def return_creds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as my_creds:
        nasa_creds = my_creds.read()
    ## remove any newline characters from the api_key
    nasa_creds = "api_key=" + nasa_creds.strip("\n")
    return nasa_creds

# this is our main function
def main():
    ## first grab credentials
    nasa_creds = return_creds()

    ## update the date below, if you like
    start_date = "start_date=2023-01-18"

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neo_request = requests.get(neo_url + start_date + "&" + nasa_creds)

    # strip off json attachment from our response
    neo_data = neo_request.json()

    ## display NASAs NEOW data
    print(neo_data)

if __name__ == "__main__":
    main()

