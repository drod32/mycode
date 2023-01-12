#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Looping across a file opened with 'with'
         while also being gentle on memory consumption."""


# open file in read mode
with open("dnsservers.txt", "r") as dns_file:
    # indent to keep the dns file object open
    # loop across the line in the file
    for server in dns_file:
        server = server.rstrip("\n")

        # if the string server endswith "org"
        if server.endswith("org"):
            with open("org-domain.txt", "a") as server_file: # 'a' is append mode
                server_file.write(server + "\n")
        elif server.endswith("com"):
            with open("com-domain.txt", "a") as server_file:
                server_file.write(server + "\n")
