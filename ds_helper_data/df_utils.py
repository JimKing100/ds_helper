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

def state_conv(st_abbrev):

  us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'District of Columbia': 'DC',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Northern Mariana Islands':'MP',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Palau': 'PW',
    'Pennsylvania': 'PA',
    'Puerto Rico': 'PR',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virgin Islands': 'VI',
    'Virginia': 'VA',
    'Washington': 'WA',
    'Washington, DC': 'DC',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
  }

  abbrev_us_state = dict(map(reversed, us_state_abbrev.items()))

  if len(st_abbrev) == 2:
    try:
      return_value = abbrev_us_state[st_abbrev]
    except KeyError:
      return_value = "NA"
  else:
    try:
      return_value = us_state_abbrev[st_abbrev]
    except KeyError:
      return_value = "NA"

  return return_value
