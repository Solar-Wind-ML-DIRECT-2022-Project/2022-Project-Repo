__version__ = "1.1"

# optimizing hyperparameters

import geopandas as gp
import pandas as pd
import optuna
import numpy as np
import sklearn
import os

from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import r2_score
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error


import json_to_csv
from json_to_csv import geojson_to_csv

import ts_train_test_split
from ts_train_test_split import uni_selection
from ts_train_test_split import single_split




def TSS(df):
    """
    splits the dataframe using timeseries splits into 11 different splits
    takes the second to last split to save as the validation split.
    takes the last split as the testing split.
    """
    X = df['ds'].values
    y = df['y'].values
    X_dict = {}
    y_dict = {}
    kmax = 11
    tss = TimeSeriesSplit(gap=0, max_train_size=None, n_splits=kmax)
    k = 0
    for train_index, test_index in tss.split(X):
        X_dev, X_test = X[train_index], X[test_index]
        y_dev, y_test = y[train_index], y[test_index]
        if k == kmax-2:
            X_train, X_val = X[train_index], X[test_index]
            y_train, y_val = y[train_index], y[test_index]
        k = k + 1

    X_dict['X_dev'] = X_dev
    X_dict['X_test'] = X_test
    X_dict['X_train'] = X_train
    X_dict['X_val'] = X_val

    y_dict['y_dev'] = y_dev
    y_dict['y_test'] = y_test
    y_dict['y_train'] = y_train
    y_dict['y_val'] = y_val

    return(X_dict, y_dict)


def r2score_TSS(sample, locations, p, d, q, P, D, Q):
    """
    Calculates the r2 score for the validation dataset, training on the
    training dataset.
    pdq: the hyperparameters for the SARIMAX model.
    """


    prediction = []

    geojson = locations['filepath'][sample]
    df = geojson_to_csv(geojson)
    X = uni_selection(df)
    X_train, X_test = single_split(X)
    X_train, X_test = single_split(X_train)
    X_train.index = pd.DatetimeIndex(X_train.index.values,
                                     freq=X_train.index.inferred_freq)
    model = SARIMAX(X_train, order=(p, d, q), seasonal_order=(P, D, Q, 12),
                    enforce_stationarity=False, enforce_invertibility=False)
    model_fit = model.fit(maxiter=60, method='powell')

#   start and end value is data dependent
    predict = model_fit.get_prediction(start='2013-01-01', end='2016-12-01')
                                  # (start='2017-01-01', end='2020-12-01')

    prediction.append(predict.predicted_mean)
    predicted = pd.DataFrame(prediction)
    predicted = predicted.T
    # MSE = mean_squared_error(X_test, predicted)
    score = r2_score(X_test, predicted)
    return score


def objective(trial, sample, locations):
    # define hyperparameter space
    p = trial.suggest_int("p", 0, 8)
    d = trial.suggest_int("d", 0, 1)
    q = trial.suggest_int("q", 0, 8)
    P = trial.suggest_int("P", 0, 3)
    D = trial.suggest_int("D", 0, 1)
    Q = trial.suggest_int("Q", 0, 3)

    # get the score for the hyperparameters chosen
    score = r2score_TSS(sample, locations, p, d, q, P, D, Q)
    return score


def study_hyper(sample, locations, n_trials=10):
    """
    optimizes the hyperparameters for SARIMAX of a dataset using a TPE sampler.
    """

    def argfunction(trial):
        objective(trial, sample, locations)

    study = optuna.create_study(
        sampler=optuna.samplers.TPESampler(), direction='maximize')
    study.optimize(argfunction, n_trials=n_trials)

    results = study.trials_dataframe()
    print(study)
    return results



