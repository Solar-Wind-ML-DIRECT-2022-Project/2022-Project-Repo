import numpy as np
import geopandas as gp
import pandas as pd
import datetime as dt
import unittest

from statsmodels.tsa.statespace.sarimax import SARIMAX

# import .py scripts from repo
from json_to_csv import geojson_to_csv
from ts_train_test_split import uni_selection
import forecast_single


locations = pd.read_csv('Final_validation.csv', index_col=0)


class TestForecast(unittest.TestCase):

    def test_inputs(self):
        '''checks that sample parameter only accepts positive integers'''
        locations = pd.read_csv('Final_validation.csv', index_col=0)
        self.assertRaises(KeyError, forecast_single.forecast,
                          locations, sample=3.3)
        self.assertRaises(KeyError, forecast_single.forecast,
                          locations, sample=-5)

    def test_output(self):
        '''checks that the output df of the function is one column
        and includes all data'''
        locations = pd.read_csv('Final_validation.csv', index_col=0)
        result = forecast_single.forecast(locations, sample=25)
        self.assertEqual(np.shape(result), (624, 1))
