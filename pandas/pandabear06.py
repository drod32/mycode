#!/usr/bin/env python3

""" Alta3 Research
in panda, a single point in time is represented as a timestamp.
we can use the to_datetime() function to create Timestamps from strings in a wide variety of date/time formats.
Let’s import pandas and convert a few dates and times to Timestamps.
"""

import pandas as panda

def main():
    """run-time code"""

    # to_datetime() automatically infers a date/time format based on the input 
    # the ambigous date "7/8/1952" is assumed to be month/day/year and is iterpreted as july 8, 1952
    print(panda.to_datetime("1993-01-23 3:45pm"))
    # 2018-01-15 15:45:00

    # Alternatively , we can use the dayfirst parameter to tell pandas to interpret the date as august 7 1952,
    print(panda.to_datetime("01/23/1993"))
    # 1952-08-07 00:00:00

    print(panda.to_datetime("23/01/1993", dayfirst=True))
    # 1952-08-07 00:00:00

    # supply a list of array of strings as input to to_datetime() and it
    # returns a sequence of date/time values in a Date_Time_Index object,
    # which is the core data structure that powers much of pandas time series functionality
    print(panda.to_datetime(["2018-01-23", "01/23/1993", "Jan 23, 1993"]))
    # DatetimeIndex(['2018-01-05', '1952-07-08', '1995-10-10'], dtype='datetime64[ns]', freq=None)
    # In the DatetimeIndex above, 
    # the data type datetime64[ns] indicates that the underlying data is stored as 64-bit integers, in units of nanoseconds (ns)
    # This data structure allows pandas to compactly store large sequences of date/time values and
    # efficiently perform vectorized operations using NumPy datetime64 arrays.

    # Dealing with a sequence of strings all in the same date/time format, we can explicitly specify it with the format parameter
    # For very large data sets, this can greatly speed up the performance of to_datetime() compared to the default behavior
    # Any of the format codes from the strftime() and strptime() functions in Python’s built-in datetime module can be used.
    print(panda.to_datetime(['01/23/93', '8/6/17', '12/15/12'], format='%m/%d/%y'))
    # DatetimeIndex(['2010-02-25', '2017-08-06', '2012-12-15'], dtype='datetime64[ns]', freq=None)

if __name__ == "__main__":
    main()


    
