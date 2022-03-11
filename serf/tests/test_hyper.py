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

filename = ("NASA/POWER_Point_Monthly_Timeseries_"
            "1981_2020_046d0562N_118d3476W_LST.json")


class test_hyperparam_opt(unittest.TestCase):

    def test_filename(self):
        assert type(filename) == str

    def test_loadjson(self):
        df = loadjson(filename)
        assert type(df) == pd.DataFrame

    def test_loadjson_nofile(self):
        with self.assertRaises(ValueError):
            loadjson('this_is_a_dummy_file_name')

    def test_rm13(self):
        df = loadjson(filename)
        df2 = rm13(df)
        assert df2.shape[0] < df.shape[0]

    def test_rm13_fail(self):
        with self.assertRaises(TypeError):
            df1 = rm13(1)

    def test_numtodate(self):
        df = loadjson(filename)
        df = rm13(df)
        df = Prophet_preproc(df)
        assert isinstance(df['ds'].values[0], str)

    def test_Pro_preproc(self):
        df = loadjson(filename)
        df = rm13(df)
        df = Prophet_preproc(df)
        assert 'y' in df

    def test_Pro_preproc_fail(self):
        with self.assertRaises(ValueError):
            df = loadjson(filename)
            df = rm13(df)
            df = Prophet_preproc(df, column_y='aaaaaa')
            return 'check 1 complete'

    def test_TSS(self):
        df = loadjson(filename)
        df = rm13(df)
        df = Prophet_preproc(df)
        X, Y = TSS(df)
        assert type(X) == dict

    def test_TSS_fail(self):
        df = loadjson(filename)
        df = rm13(df)
        df = Prophet_preproc(df)
        with self.assertRaises(TypeError):
            X, Y = TSS(1)

    '''
    this is an intensive test, only run when necessary
    def test_hyper_study(self):
        df = loadjson(filename)
        df = rm13(df)
        df = Prophet_preproc(df)
        X, y = TSS(df)
        results = study_hyper(y['y_train'], y['y_val'], n_trials=1)
        return
    '''

    def test_r2(self):
        df = loadjson(filename)
        df = rm13(df)
        df = Prophet_preproc(df)
        X, y = TSS(df)
        score = r2score_TSS(y['y_train'], y['y_val'], 6, 1, 3, 1, 0, 1)
        assert isinstance(score, float)
