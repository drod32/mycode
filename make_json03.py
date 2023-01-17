#!/usr/bin/python3
"""opening a static file containing JSON data | Alta3 Research"""

# JSON is part of the Python Standard Library
import json

def main():
    """runtime code"""
    ## open the file
    with open("datacenter.json", "r") as datacenter:
        datacenter_string = datacenter.read()

    ## display our decoded string
    print(datacenter_string)
    print(type(datacenter_string))           
    print("\nThe code above is string data. Python cannot easily work with this data.")
    input("Press Enter to continue\n")            

    ## Create the JSON string
    datacenter_decoded = json.loads(datacenter_string)

    ## This is now a dictionary
    print(type(datacenter_decoded))

    ## display the servers in the datacenter
    print(datacenter_decoded)

    ## display the servers in row3
    print(datacenter_decoded["row3"])

    ## display the 2nd server in row2
    print(datacenter_decoded["row2"][1])

    ## write code to
    ## display the last server in row3

if __name__ == "__main__":
    main()

