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
from model_validation import model_val

import model_testing_function

locations = pd.read_csv('Final_validation.csv')

'''class TestModelTestingFunction(unittest.TestCase):
    
    def test_output(self):
        '''#is the output shape correct?'''
        locations = pd.read_csv('Final_validation.csv')
        results = model_testing_function.test_all(locations)
        self.assertEqual(np.shape(results), (27, 2))
        self.assertIsInstance(results, pd.core.frame.DataFrame)'''