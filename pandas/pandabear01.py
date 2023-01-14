#!/usr/bin/env python3

"""Alta3 Research.... 
    Exploring using panda to create dataframes and output graphs"""

import pandas as panda

def main():
    # define name of .xls file
    excel_file = "movies.xls"

    # create a DataFrame (DF) object. 
    # because we did not specify a sheet
    # only the first sheet was read into the DF
    movies = panda.read_excel(excel_file)

    # show the first five rows of our DF
    # DF has a 5 rows and 25 columns (index by integer)
    print(movies.head())

    # Choose the first column "title" as
    # index(index=0)
    movie_sheet1 = panda.read_excel(excel_file, sheet_name=0, index_col=0)

    # DF has 5 rows and 24 columns (indexed by title)
    # print the top 10 movies in the dataframe
    print(movie_sheet1.head())

    # export 5 movies from the top dataframe to excel
    movie_sheet1.head(5).to_excel("5movies.xlsx")

    # export 5 to json
    movie_sheet1.head(5).to_json("5movies.json")

    # export 5 to .csv
    movie_sheet1.head(5).to_csv("5movies.csv")


if __name__ == "__main__":
    main()


