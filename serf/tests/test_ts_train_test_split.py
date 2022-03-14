import unittest
from json_to_csv import *
from ts_train_test_split import *

import numpy as np
import geopandas as gp
import pandas as pd
import datetime as dt


sample = ('NASA/POWER_Point_Monthly_Timeseries_1981'
          '_2020_047d9735N_122d2038W_LST.json')
df = geojson_to_csv(sample)
X = uni_selection(df)


class TestTSSplit(unittest.TestCase):

    def test_uniselection(self):
        # from the pandas df does it create a new DataFrame
        sample = ('NASA/POWER_Point_Monthly_Timeseries_1981_2020'
                  '_047d9735N_122d2038W_LST.json')
        df = geojson_to_csv(sample)
        self.assertRaises(TypeError, uni_selection, df, 'ALLSKY_KT')

    def test_uni_fail(self):
        df = 'a'
        with self.assertRaises(TypeError):
            uni_selection(df)

    def test_unit_pass(self):
        df = geojson_to_csv(sample)
        assert type(uni_selection(df)) == pd.DataFrame

    def test_split(self):
        # split dataset with reasonable numbers
        sample = ('NASA/POWER_Point_Monthly_Timeseries_1981_2020'
                  '_047d9735N_122d2038W_LST.json')
        df = json_to_csv.geojson_to_csv(sample)
        X = uni_selection(df)
        self.assertRaises(ValueError, single_split, X, test_size=-2)
        self.assertRaises(ValueError, single_split, X, test_size=2.3)
        self.assertRaises(ValueError, single_split, X, test_size=350)

    def test_split_pass(self):
        X1, X2 = single_split(df)
        assert type(X1) == pd.DataFrame
        assert type(X2) == pd.DataFrame

    def test_split_NaN(self):
        with self.assertRaises(ValueError):
            single_split('a')
