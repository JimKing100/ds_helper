"""
utility functions for working with DataFrames
"""

import pandas
from datetime import datetime

TEST_DF = pandas.DataFrame([1,2,3])

def nulls(df):
  columns = list(df)
  col_num = 0
  print('Nulls by Column')

  for i in columns:
    print(columns[col_num], df[i].isna().sum())
    col_num = col_num + 1

def date_conv(df, col):
  df[col] = pandas.to_datetime(df[col], infer_datetime_format=True)
  col_year = col + '_year'
  col_month = col + '_month'
  col_day = col + '_day'
  df[col_year] = df[col].dt.year
  df[col_month] = df[col].dt.month
  df[col_day] = df[col].dt.day
  return df
