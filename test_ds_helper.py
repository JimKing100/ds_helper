# import pytest
import pandas as pd
from ds_helper_data import df_utils


def test_nulls():
    df = pd.read_csv('https://raw.githubusercontent.com/JimKing100/DS-Unit-3-Sprint-1-Software-Engineering/master/module1-python-modules-packages-and-environments/drink_test.csv')
    assert df_utils.nulls(df) is None


def test_date_conv():
    df = pd.read_csv('https://raw.githubusercontent.com/JimKing100/DS-Unit-3-Sprint-1-Software-Engineering/master/module1-python-modules-packages-and-environments/MarinSalesJanJune2019.csv')
    df_utils.date_conv(df, 'Listing Date')
    assert 'Listing Date_year' in df.columns


def test_state_conv():
    assert df_utils.state_conv('California') == "CA"
