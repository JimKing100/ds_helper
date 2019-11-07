# ds_helper
A collection of data science helper functions.

## Structure

ds_helper - contains the complete implementation of the package.

ds_helper_data - contains the __init__.py file and the df_utils.py file

df_utils.py - contains the python code for the helper functions.

pipfile - adds the numpy and pandas denpendencies

setup.py - the build setup file

test_ds_helper.py - the unit test code

## Functions

TEST_DF - runs a simple test creating a DataFrame with the values 1, 2, 3.

nulls(df) - creates a nice printout of the nulls by column in a dataframe.

date_conv(df, col) - converts a column from day/month/year to 3 individual columns - day, month, year

state_conv(st_abbrev) - converts a state abbreviation to a full state name and vice-versa.


