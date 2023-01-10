#!/usr/bin/env python3
"""understanding Dictionaries
    {key:value, key:value, ...}"""

def main():
    """runtime function"""

    ##Create a dictionary with 4 key:value pairs
    switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

    ## display entire dictionary
    print(switch)

    ## prove that switch is indeed a dictionary
    print(type(switch))

    ## display parts of dictionary
    print(switch["hostname"])  #  display "sw1"
    print(switch["ip"])        # displays "10.0.1.1"

    ## request fake key
    print(switch["lynx"])      # this will cause the program to fail


if __name__ == "__main__":
    main()


