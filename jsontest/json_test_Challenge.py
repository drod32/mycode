#!/usr/bin/python3

import requests

# define the URLs we want to use
VALIDATE_URL = "http://validate.jsontest.com/"
TIME_URL = "http://date.jsontest.com"
IP_URL = "http://ip.jsontest.com"

def time_stamp():
    time_response = requests.get(TIME_URL)
    time_stamp = time_response.json()

    return time_stamp

def IP_address():
    IP_response = requests.get(IP_URL)
    IP_address = IP_response.json()

    return IP_address

def validate_my_servers():
    with open("/home/student/mycode/jsontest/my_servers.txt") as my_file:
        my_servers = my_file.readlines()
    
    return my_servers

def main():
    formatted_json = {}
    formatted_json["time"] = time_stamp()
    formatted_json["IP"] = IP_address()
    formatted_json["my_servers"] = validate_my_servers()

    my_data = {}
    my_data["json"] = str(formatted_json)

    response = requests.post(VALIDATE_URL, data=my_data)
    response_json = response.json()

    print(response_json)

    print(f"Is your JSON valid? {response_json['validate']}")

if __name__ == "__main__":
    main()

