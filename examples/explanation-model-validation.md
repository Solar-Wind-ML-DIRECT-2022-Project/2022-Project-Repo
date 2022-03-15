## Explaining the functions in the model_validation.py

These functions utilize the ``ts_train_test_split.py`` functions and refer to a csv containing the metadata for each location.

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

### Validating a single model

Both functions, ``model_val`` and ``predict_test`` reference a csv/pandas dataframe that contains filepaths and hyperparameters for each location. ``sample`` is the desired location for validating, referenced by the index location in the csv/pandas dataframe. Model hyperparameters are selected from the ``sample`` row in the df and are location-specific.

The fitted model is used to predict solar insolance for the last 48 months of in-sample dates (same as the test size specified in the ``single_split`` function). 

``model_val`` outputs the MSE and r2 score calculated from the predicted values and the X_test values.

    def model_val(locations, sample):
        '''use pd.read_csv('Locations_2.csv') to access required data.
        Sample must be integer index of desired location.
        inputs hyperparameters and fits model with training set,
        predicts last 48 months, calculates MSE and r2 of predicted values
        against X_test (48 months)'''
        prediction = []

        geojson = locations['filepath'][sample]
        df = geojson_to_csv(geojson)
        X = uni_selection(df)
        X_train, X_test = single_split(X)
        X_train.index = pd.DatetimeIndex(X_train.index.values,
                                         freq=X_train.index.inferred_freq)
        (p, d, q) = (locations['p'][sample],
                     locations['d'][sample], locations['q'][sample])
        (P, D, Q, s) = (locations['P'][sample],
                        locations['D'][sample], locations['Q'][sample], 12)
        model = SARIMAX(X_train, order=(p, d, q), seasonal_order=(P, D, Q, s))
        model_fit = model.fit(maxiter=50, method='powell', disp=False)
        predict = model_fit.get_prediction(start='2017-01-01', end='2020-12-01')

        prediction.append(predict.predicted_mean)
        predicted = pd.DataFrame(prediction)
        predicted = predicted.T
        MSE = mean_squared_error(X_test, predicted)
        r2 = r2_score(X_test, predicted)
        return MSE, r2

``predict_test`` contains the same code as ``model_val`` but returns a different output. This function returns the ``X_test`` sample and the model-predicted values in the same time range, both as DataFrames.

    def predict_test(locations, sample):
        '''use pd.read_csv('Locations_2.csv') to access required data.
        Sample must be integer index of desired location.
        inputs hyperparameters and fits model with training set,
        predicts last 48 months, returns X_test df, predicted values df'''

        prediction = []
        geojson = locations['filepath'][sample]
        df = geojson_to_csv(geojson)
        X = uni_selection(df)
        X_train, X_test = single_split(X)
        X_train.index = pd.DatetimeIndex(X_train.index.values,
                                         freq=X_train.index.inferred_freq)
        (p, d, q) = (locations['p'][sample],
                     locations['d'][sample], locations['q'][sample])
        (P, D, Q, s) = (locations['P'][sample],
                        locations['D'][sample], locations['Q'][sample], 12)
        model = SARIMAX(X_train, order=(p, d, q), seasonal_order=(P, D, Q, s),
                        enforce_stationarity=False, enforce_invertibility=False)
        model_fit = model.fit(maxiter=50, method='powell', disp=False)
        predict = model_fit.get_prediction(start='2017-01-01', end='2020-12-01')

        prediction.append(predict.predicted_mean)
        predicted = pd.DataFrame(prediction)
        predicted = predicted.T
        MSE = mean_squared_error(X_test, predicted)
        r2 = r2_score(X_test, predicted)
        return X_test, predicted
