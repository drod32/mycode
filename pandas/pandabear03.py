#!/usr/bin/python3

import pandas as panda

def main():
    cisco_csv = panda.read_csv("ciscodata.csv")
    cisco_json = panda.read_json("ciscodata2.json")

    # display first 5 entries of the ciscocsv data frame
    print(cisco_csv.head())

    # first five entries of ciscojson dataframe
    print(cisco_json.head())

    cisco_data_frame = panda.concat([cisco_csv, cisco_json])
    # uncomment the line below to "fix" the index issue
    # cisco_data_frame = panda.concat([cisco_csv, cisco_json], ignore_index=True, sort=False)

    print(cisco_data_frame)


if __name__ == "__main__":
    main()


