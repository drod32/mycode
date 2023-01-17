#!/usr/bin/env python3


def main():
    bottles_remaining = 99
    for bottles in range(100):
        print(f"{bottles_remaining} bottle of beer wall! {bottles_remaining} bottle of beer! you take one down, pass it around...")
        bottles_remaining -= 1
        print(f"{bottles_remaining} bottle of beer wall")


main()

        
        
