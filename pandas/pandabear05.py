#!/usr/bin/env python3

import pandas as panda

def main():
    # create a dataframe cisco_csv 
    cisco_csv =  panda.read_csv("ciscodata.csv")
    # create a dataframe cosco_json
    cisco_json = panda.read_json("ciscodata2.json")

    # the line below concats and reapplies the index value
    cisco_df = panda.concat([cisco_csv, cisco_json], ignore_index=True, sort=False)

    # export to csv
    # do not include index numbers 
    cisco_df.to_json("combined_ciscodata.json", orient="records")

    # export to csv
    # do not include index number
    cisco_df.to_csv("combined_ciscodata.csv", index=False)

    # export to excel
    # do not include index number to xls
    cisco_df.to_excel("combined_ciscodata.xls", index=False)
    # do the same to xlsx
    cisco_df.to_excel("combined_ciscodata.xlsx", index=False)

    # create a python dictionary
    # do not include index number 
    python_dictionary = cisco_df.to_dict(orient="records")
    print(python_dictionary)

if __name__ == "__main__":
    main()


