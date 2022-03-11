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

def model_validation(locations, sample):
    '''use pd.read_csv('Locations.csv') to access required data. 
    Sample must be integer index of desired location.
    inputs hyperparameters and fits model with training set, predicts last 48 months,
    calculates MSE and r2 of predicted values against X_testv (48 months)'''
    prediction = []
    ci = []
    
    geojson = locations['filepath'][sample]
    df = geojson_to_csv(geojson)
    X = uni_selection(df)
    X_train, X_test = single_split(X)
    X_train.index = pd.DatetimeIndex(X_train.index.values,
                                     freq=X_train.index.inferred_freq)
    (p,d,q) = (locations['p'][sample],locations['d'][sample],locations['q'][sample])
    (P,D,Q,s) = (locations['P'][sample],locations['D'][sample],locations['Q'][sample],12)
    model = SARIMAX(X_train, order = (p,d,q), seasonal_order = (P,D,Q,s))
    model_fit = model.fit(disp = False)
    predict = model_fit.get_prediction(start='2017-01-01', end='2020-12-01')
    predict_ci = predict.conf_int()
    
    prediction.append(predict.predicted_mean)
    predicted = pd.DataFrame(prediction)
    predicted = predicted.T
    ci.append(predict_ci)
    MSE = mean_squared_error(X_test, predicted)
    r2 = r2_score(X_test, predicted)
    return predicted, ci, MSE, r2