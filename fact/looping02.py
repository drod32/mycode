#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Using a file's lines as a source for the for-loop"""

# open file in read mode
dnsfile = open("dnsservers.txt", "r")

# create a list of lines
dnslist  = dnsfile.readlines()

# loop over lines
for server in dnslist:
    # print and end without a new line
    print(server, end="") # the line we read ALREADY contains a \n (newline)

# close the file
dnsfile.close()

