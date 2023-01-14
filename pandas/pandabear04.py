#!/usr/bin/env python3

import pandas as panda

def main():
    # create a dataframe ciscosv
    cisco_csv = panda.read_csv("ciscodata.csv")
    # create a dataframe cisco_json
    cisco_json = panda.read_json("ciscodata2.json")

    # the line below concats an reapplies index values
    cisco_data_frame = panda.concat([cisco_csv, cisco_json], ignore_index=True, sort=False)

    #print the re-indexed dataframe
    print(f"\n{cisco_data_frame}\n")

    # export json
    cisco_data_frame.to_json("combined_ciscodata.json")

    # export csv
    cisco_data_frame.to_csv("combined_ciscodata.csv")

    # export to excel
    cisco_data_frame.to_excel("combined_ciscodata.xls")

    # create a python dictionary
    python_dictionary = cisco_data_frame.to_dict()
    print(python_dictionary)


if __name__ == "__main__":
    main()

