#!/usr/bin/env python3
"""Marvel Python Client
RZFeeser@alta3.com | Alta3 Research"""

# standard imports
import argparse  # pull in arguments from CLI
import time      # create Time Stamps
import hashlib   # create md5 hash to pass to marvel
from pprint import pprint # this only imports pprint() from the entire pprint package

# 3rd party imports
import requests

# api base URL
marvel_api_url = "http://gateway.marvel.com/v1/public/characters"

## Calculate a hash to pass through to our MARVEL API call
## Marvel API wants md5 calc md5(ts+privateKey+publicKey)
def hash_builder(rand, private_key, public_key):
    return hashlib.md5((f"{rand}{private_key}{public_key}").encode("utf-8")).hexdigest() # create MD5 hash

## Perform a call to MARVEL Character API
## http://gateway.marvel.com/v1/public/characters
## ?name=Spider-Man&ts=1&apikey=1234&hash=ffd275c5130566a2916217b101f26150
def marvel_character_call(rand, key_hash, public_key, look_me_up):
    request = requests.get(f"{marvel_api_url}?name={look_me_up}&ts={rand}&apikey={public_key}&hash={key_hash}")

    # the marvel APIs are "flakey" at best, so check for a 200 response
    if request.status_code != 200:
        response = None     #
    else:
        response = request.json()

    # return the HTTP response with the JSON removed
    return response

def main():

    ## harvest private key
    with open(args.dev) as private_key:
        private_key = private_key.read().rstrip('\n')

    ## harvest public key
    with open(args.pub) as public_key:
        public_key = public_key.read().rstrip('\n')

    rand = str(time.time()).rstrip('.')

     ## build hash with hash_builder
    key_hash = hash_builder(rand, private_key, public_key)

    ## call the API with marvelcharcall(timestamp, hash, publickey, character)
    result = marvel_character_call(rand, key_hash, public_key, args.hero)

    ## display results
    pprint(result)

    ## Define arguments to collect
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # This allows us to pass in public and private keys
    parser.add_argument('--dev', help='Provide the /path/to/file.priv containing Marvel private developer key')
    parser.add_argument('--pub', help='Provide the /path/to/file.pub containing Marvel public developer key')
    parser.add_argument('--hero', help='Character to search for within the Marvel universe')
    args = parser.parse_args()
    main()
