#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   Exploring using pandas to create graphs"""

import pandas as panda

# these following two lines are for writing to file
# use this when you are not rendering to a windo
import matplotlib
matplotlib.use("Agg")

# lets create some graphs
import matplotlib.pyplot as plot

def main():
    # define the name of our xls file
    excel_file = "movies.xls"
    
    # choose the first column "Title"
    # index (index = 0)
    movie_sheet1 = panda.read_excel(excel_file, sheet_name=0, index_col=0)
    # DF has 5 rows and 24 columns (indexed by title)
    print(movie_sheet1.head())

    # grab the next 2 sheets as well
    movie_sheet2 = panda.read_excel(excel_file, sheet_name=1, index_col=0)
    print(movie_sheet2.head())

    movie_sheet3 = panda.read_excel(excel_file, sheet_name=2, index_col=0)
    print(movie_sheet3.head())

    # combine all DFs into a single DF called movies
    movies = panda.concat([movie_sheet1, movie_sheet2, movie_sheet3])

    # number of rows and columns (5042, 24)
    print(movies.shape)

    # unfortunately our data has some duplicates
    # we can remove them quickly with .drop_duplicate() method
    movies.drop_duplicates(inplace=True)
    
    # take peek at how the Data Frame changed
    print(movies.shape)

    # sort data frames based on gross earnings
    sorted_by_gross = movies.sort_values(["Gross Earnings"], ascending=False)

    # data is sorted by valuse in a column
    # display the top 10 Grossing movies
    # pasing the 10 values to head returns the top 10 not the default 5
    print(sorted_by_gross.head(10))

    # create a stacked bar graph
    sorted_by_gross["Gross Earnings"].head(10).plot(kind="barh")
    # save figure as stackbar.png 

    plot.savefig("/home/student/static/stackedbar.png", bbox_inches="tight")


if __name__ == "__main__":
    main()



