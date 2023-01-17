#!/usr/bin/python3
"""opening a static file containing JSON data | Alta3 Research"""

# JSON is part of the Python Standard Library
import json

def main():
    """runtime code"""
    ## open the file
    with open("datacenter.json", "r") as datacenter:
        datacenter_decoded = json.load(datacenter)

    ## This is now a dictionary
    print(type(datacenter_decoded))

    ## display the servers in the datacenter
    print(datacenter_decoded)

    ## display the servers in row3
    print(datacenter_decoded["row3"])

    ## display the 2nd server in row2
    print(datacenter_decoded["row2"][1])

if __name__ == "__main__":
    main()

