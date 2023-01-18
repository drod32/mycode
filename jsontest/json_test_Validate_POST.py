#!/usr/bin/python3

import requests

# define the URL we want to use
POSTURL = "http://validate.jsontest.com/"

def main():
    # test data to validate as legal json
    # when a POST json= is replaced by the KEY "json"
    # the key "json" is mapped to a VALUE of the json to test
    # because the test item is a string, we can include whitespaces
    my_data = {"json": "{'fruit': ['apple', 'pear'], 'vegetable': ['carrot']}" }

    # use requests library to send an HTTP POST
    response = requests.post(POSTURL, data=my_data)

    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    response_json = response.json()

    # display our PYTHONIC data (LIST / DICT)
    print(response_json)

    # JUST display the value of "validate"
    print(f"Is your JSON valid? {response_json['validate']}")

if __name__ == "__main__":
    main()

