#!/usr/bin/python3
"""Alta3 Research - astros on ISS"""

import urllib.request
import json

MAJOR_TOM = "http://api.open-notify.org/astros.json"

def main():
    """reading json from API"""

    # call api
    ground_control = urllib.request.urlopen(MAJOR_TOM)

    # strip attached json and read
    # the problem here, is that it will read out as a string
    helmet = ground_control.read()
    
    # show that at this point, our data is str
    # we want to convert this to list / dict
    print(helmet)

    helmet_json = json.loads(helmet.decode("utf-8"))

    print(type(helmet))
    print(type(helmet_json))

    print(helmet_json["number"])

    # this returns a LIST of the people on this ISS
    print(helmet_json["people"])

    # list the FIRST astro in the list
    print(helmet_json["people"][0])

    # list the SECOND astro in the list
    print(helmet_json["people"][1])

    # list the LAST astro in the list
    print(helmet_json["people"][-1])

    # display every item in a list
    for astro in helmet_json["people"]:
        # display what astro is
        print(astro)

if __name__ == "__main__":
    main()

