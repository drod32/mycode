#!/usr/bin/env python3 

## create file object in "r"ead mode
with open("vlanconfig.cfg", "r") as configfile:

    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

## file was just aut cclosed because of with
print(configlist)
