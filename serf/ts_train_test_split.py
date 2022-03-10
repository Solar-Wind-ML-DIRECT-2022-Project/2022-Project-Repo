import numpy as np
import geopandas as gp
import pandas as pd

import datetime as dt

import json_to_csv


def uni_selection(df, variable=['ALLSKY_KT']):
    '''for univariate SARIMAX model, creates a new df with solar index'''
    X = df[variable]
    if type(X) != pd.DataFrame:
        raise TypeError('X is pd.Series, not DataFrame. Check parameters.')
    else: pass
    return(X)

def single_split(X, test_size=48):
    '''performs a time-series split on dataset with test size of 48 months,
    or as desired'''
    if test_size < 1 or not isinstance(test_size, int):
        raise ValueError('test size must be positive integer.')
    elif test_size > round(len(X)*.4):
        raise ValueError('test size is large (> 40% dataset) ')
    else:
        X_train = X[:-test_size]
        X_test = X[-test_size:]
    return(X_train, X_test)