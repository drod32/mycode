#!/usr/bin/python3

import requests
import json

# define the URL we want to use
GETURL = "http://validate.jsontest.com/"

def main():
    # test data to validate as legal json
    my_data = {"fruit": ["apple", "pear"], "vegetable": ["carrot"]}

    ## the next two lines do the same thing
    ## we take python, convert to a string, then strip out whitespace
    #jsonToValidate = "json=" + str(mydata).replace(" ", "")
    #jsonToValidate = f"json={ str(mydata).replace(' ', '') }"
    ## slightly different thinking
    ## user json library to convert to legal json, then strip out whitespace
    json_to_validate = f"json={ json.dumps(my_data).replace(' ', '') }"

    # use requests library to send an HTTP GET
    response = requests.get(f"{GETURL}?{json_to_validate}")

    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    response_json = response.json()

    # display our PYTHONIC data (LIST / DICT)
    print(response_json)

    # JUST display the value of "validate"
    print(f"Is your JSON valid? {response_json['validate']}")

if __name__ == "__main__":
    main()

