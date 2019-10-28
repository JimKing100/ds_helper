"""
utility functions for working with DataFrames
"""

import pandas

TEST_DF = pandas.DataFrame([1,2,3])

def NULLS(df):
  columns = list(df)
  col_num = 0
  print('Nulls by Column')

  for i in columns:
    print(columns[col_num], df[i].isna().sum())
    col_num = col_num + 1
