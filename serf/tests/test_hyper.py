from json import load
import unittest
import pandas as pd
import numpy as pd
import geopandas as gp
import optuna
from statsmodels.tsa.statespace.sarimax import SARIMAX

import sklearn
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import r2_score

from hyperparam_opt import *

filename = '''NASA/POWER_Point_Monthly_Timeseries_1981_2020_046d0562N_118d3476W_LST.json'''

class test_hyperparam_opt(unittest.TestCase):

    def test_test(self):
        assert type(filename)==str

    def test_loadjson(self):
        df = loadjson(filename)
        assert type(df) ==pd.DataFrame

    def test_rm13(self):
        df = loadjson(filename)
        df2 = rm13(df)
        assert df2.shape[0] < df.shape[0]

#    def test_numtodate(self):
#        df = loadjson(filename)
#        df = rm13(df)

    def test_Pro_preproc(self):
        df = loadjson(filename)
        df = rm13(df)
        df = Prophet_preproc(df)
        assert 'y' in df     