#!/usr/bin/env python3
## create file object in "r"ead mode
configfile = open("vlanconfig.cfg", "r")

## display file to the screen - .read()
configblog = configfile.read()

## break the configblog across line boundaries(strip out /n)
configlist = configblog.splitlines()

## display lis with no "/n"
print(configlist)

## dont forget to close your file
configfile.close()

