#!/usr/bin/env python3

import requests

api_url = "https://pokeapi.co/api/v2/pokemon/"

def main():
    poke_number = input("pick a number between 1 and 151!\n>>>")
    poke_api = requests.get(api_url + poke_number).json()

    print(poke_api["sprites"]["front_default"])
    
    for moves in poke_api['moves']:
        print(moves['move']['name'])

    length_of_game_indices = len(poke_api["game_indices"])
    print(length_of_game_indices)

    index = 0
    for game_appearances in poke_api["game_indices"]:
        index += 1
    print(index)

main()
