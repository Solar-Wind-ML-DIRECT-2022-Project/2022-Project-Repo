import numpy as np
import geopandas as gp
import pandas as pd
import datetime as dt

from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# import .py scripts from repo
import json_to_csv
from json_to_csv import geojson_to_csv

import ts_train_test_split
from ts_train_test_split import uni_selection
from ts_train_test_split import single_split
from model_validation import model_val


def test_all(locations):
    '''time-series splits the ALLSKY_KT data into X_train, X_test,
    fits model with X_train and opt hyperparams,
    compares to X_test and returns MSE, r2 for each row in Locations_2.csv'''
    MSEs = []
    r2s = []
    for row in range(len(locations)):
        MSE, r2 = model_val(locations, sample=row)
        MSEs.append(MSE)
        r2s.append(r2)
    MSEs = pd.DataFrame([MSEs]).T
    r2s = pd.DataFrame([r2s]).T
    results = pd.concat([MSEs, r2s], keys=['MSE', 'r2'], axis=1)
    results.columns = results.columns.droplevel(1)
    return(results)


def append_results(locations, results):
    '''adds results from test_all function to a
    df with Locations_2.csv information'''
    accuracy = pd.concat([locations, results], axis=1)
    return(accuracy)
