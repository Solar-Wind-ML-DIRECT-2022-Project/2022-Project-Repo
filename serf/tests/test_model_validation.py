import numpy as np
import geopandas as gp
import pandas as pd
import datetime as dt
import unittest

from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# import .py scripts from repo
from json_to_csv import geojson_to_csv
from ts_train_test_split import uni_selection
from ts_train_test_split import single_split

# import .py scripts to test
import model_validation

locations = pd.read_csv('Final_validation.csv', index_col=0)


class TestModelValidation(unittest.TestCase):

    def test_inputs(self):
        '''check that the functions only accept positive int.'''
        locations = pd.read_csv('Final_validation.csv', index_col=0)
        self.assertRaises(KeyError, model_validation.model_val,
                          locations, sample=3.3)
        self.assertRaises(KeyError, model_validation.model_val,
                          locations, sample=-5)
        self.assertRaises(KeyError, model_validation.predict_test,
                          locations, sample=3.3)
        self.assertRaises(KeyError, model_validation.predict_test,
                          locations, sample=-5)

    def test_df_outputs(self):
        '''check that the function outputs df of correct size'''
        locations = pd.read_csv('Final_validation.csv', index_col=0)
        X_test, predict = model_validation.predict_test(locations,
                                                        sample=25)
        self.assertEqual(np.shape(X_test), (48, 1))
        self.assertEqual(np.shape(predict), (48, 1))

    def test_accuracy_outputs(self):
        '''Are the r2 and MSE scores reasonable?'''
        locations = pd.read_csv('Final_validation.csv', index_col=0)
        MSE, r2 = model_validation.model_val(locations, sample=25)
        self.assertGreater(MSE, 0)
        self.assertGreater(r2, 0)
        self.assertLessEqual(r2, 1)
