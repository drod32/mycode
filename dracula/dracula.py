#!/usr/bin/env python3 


#open dracula txt file

with open("dracula.txt", "r") as og_document:
    with open("vampire.txt", "w") as new_document:
        i=0
        for line in og_document:
            if line.lower().__contains__("vampire"):
                i += 1
                new_document.write(line)
                print(line)

print(f"Number of lines: {i})")

