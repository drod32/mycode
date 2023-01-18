#!/usr/bin/python3
"""tracking the iss using
   api.open-notify.org/astros.json | Alta3 Research"""

# notice we no longer need to import urllib.request or json
import requests

## Define URL
MAJOR_TOM = 'http://api.open-notify.org/astros.json'

def main():
    """runtime code"""

    ## Call the webservice
    ground_control = requests.get(MAJOR_TOM)
    # send a post with requests.post()
    # send a put with requests.put()
    # send a delete with requests.delete()
    # send a head with requests.head()

    ## strip the json off the 200 that was returned by our API
    ## translate the json into python lists and dictionaries
    helmet_json = ground_control.json()

    ## display our Pythonic data
    print("\n\nConverted Python data")
    print(helmet_json)

    print('\n\nPeople in Space: ', helmet_json['number'])
    people = helmet_json['people']
    print(f"{people}\n")

    for astronauts in helmet_json["people"]:
        print(f"{astronauts['name']} on the {astronauts['craft']}")


if __name__ == "__main__":
    main()
