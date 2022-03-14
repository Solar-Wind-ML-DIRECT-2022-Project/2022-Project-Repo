import numpy as np
import pandas as pd
import datetime as dt
import unittest
from forecast_single import forecast
from arima_dataframe import arima_results
from arima_yearly_averages import arima_averages


locations = pd.read_csv('Locations_2.csv')


class Testplotly(unittest.TestCase):

    def test_arima_results(self):
        df = forecast(locations, (1))
        df = arima_results(df)
        assert 'Year' in df

    def test_arima_results_fail(self):
        with self.assertRaises(TypeError):
            arima_results('a')

    def test_forecast(self):
       df = forecast(locations, (2))
       assert df.shape[0] > 444

    def test_arima_averages(self):
        df = forecast(locations, (1))
        df = arima_results(df)
        df = arima_averages(df)
        assert 'Year' in df
        assert 'Solar Ratio' in df

    def test_arima_averages_wrongdf(self):
        df = forecast(locations, (1))
        with self.assertRaises(KeyError):
            df = arima_averages(df)
 