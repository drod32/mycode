#!/usr/bin/env python3

import crayons

# function to push commands
def commandpush(devicecmd): # devicecmd == dictionary

    for ip in devicecmd.keys(): #loops through the dict
        print(f"Handshaking.. .. ... connecting with {ip}")

        for mycmds in devicecmd[ip]:
            print(f"Attempting to sending command --> {mycmds}")

    return None

def devicereboot(ip_addressbook):

    for ip in ip_addressbook:
        print(f"Connecting to {ip}, Rebooting Now!")

def main():
    """called at runtime"""
    
    # dict containing IPs mapped to a list of physical interfaces and their state
    devicecmd = {"10.1.0.1":["interface eth1/2", "no shutdown"], "10.2.0.1":
    ["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]}

    
    print(f"{crayons.green('Welcome to the network device command pusher', bold=True)}")

    ## get data set
    print("\nData set found\n")

    ##run
    commandpush(devicecmd)  # call function to push commands to devices

#call main function
main()

