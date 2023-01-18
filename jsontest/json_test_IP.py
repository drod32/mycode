#!/usr/bin/python3

import requests

# define the URL we want to use
IP_URL = "http://ip.jsontest.com/"

def main():
    # use requests library to send an HTTP GET
    request = requests.get(IP_URL)

    # strip off JSON response
    # and convert to PYTHONIC LIST / DICT
    response_json = request.json()

    # display our PYTHONIC data (LIST / DICT)
    print(response_json)

    # JUST display the value of "ip"
    print(f"The current WAN IP is --> {response_json['ip']}")

if __name__ == "__main__":
    main()

