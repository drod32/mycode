#!/usr/bin/env python3


challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]


# Challenge 
def slice_challenge():
    a = challenge[2][1]
    b = challenge[2][0]
    c = challenge[3]
    print(f"My {a}! The {b} do {c}!")

# trial
def slice_trial():
    a = trial[2]["goggles"]
    b = trial[2]["eyes"]
    c = trial[3]
    print(f"My {a}! The {b} do {c}!")

#nightmare
def slice_nightmare():
    a = nightmare[0]["user"]["name"]["first"]
    b = nightmare[0]["kumquat"]
    c = nightmare[0]["d"]
    print(f"My {a}! The {b} do {c}!")

slice_challenge()
slice_trial()
slice_nightmare()
