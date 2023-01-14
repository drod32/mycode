#!/usr/bin/env python3

""" Alta 3 Research | 
    Challenge Solution 01 Json To Csv:"""


import pandas 

def main():

    # create a dataframe from json
    data_frame = pandas.read_json("5movies.json")

    #write to csv
    data_frame.to_csv("5movies-translated-from-json.csv")

if __name__ == "__main__":
    main()


