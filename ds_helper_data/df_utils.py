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
  df[col] = pd.to_datetime(df[col], infer_datetime_format=True)
  df['year'] = df[col].dt.year
  df['month'] = df[col].dt.month
  df['day'] = df[col].dt.day
  return df
