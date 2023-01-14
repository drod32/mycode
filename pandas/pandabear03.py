#!/usr/bin/python3

import pandas as panda

def main():
    ciscocsv = panda.read_csv("ciscodata.csv")
    ciscojson = panda.read_json("ciscodata2.json")

    # display first 5 entries of the ciscocsv data frame
    print(ciscocsv.head())

    # first five entries of ciscojson dataframe
    print(ciscojson.head())

    ciscodf = panda.concat([ciscocsv, ciscojson])
    # uncomment the line below to "fix" the index issue
    # ciscodf = pd.concat([ciscocsv, ciscojson], ignore_index=True, sort=False)

    print(ciscodf)


if __name__ == "__main__":
    main()


