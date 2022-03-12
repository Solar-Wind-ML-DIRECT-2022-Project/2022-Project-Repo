import numpy as np
import geopandas as gp
import pandas as pd
import datetime as dt

from statsmodels.tsa.statespace.sarimax import SARIMAX

# import .py scripts from repo
from json_to_csv import geojson_to_csv
from ts_train_test_split import uni_selection


def forecast(locations, sample):
    '''use pd.read_csv('Locations.csv') to access required data.
    Sample must be integer index of desired location.
    Fits model with input data and forecasts to 2035.
    Returns a df with real and forecasted values (1984-2035).
    results[:443] = real values, results[443:] = forecasted.'''

    forecasted = []
    geojson = locations['filepath'][sample]
    df = geojson_to_csv(geojson)
    X = uni_selection(df)
    X.index = pd.DatetimeIndex(X.index.values,
                               freq=X.index.inferred_freq)
    (p, d, q) = (locations['p'][sample],
                 locations['d'][sample], locations['q'][sample])
    (P, D, Q, s) = (locations['P'][sample],
                    locations['D'][sample], locations['Q'][sample], 12)
    model = SARIMAX(X, order=(p, d, q), seasonal_order=(P, D, Q, s))
    fit_model = model.fit(maxiter=50, method='powell', disp=False)
    forecast = fit_model.get_prediction(start='2021-01-01', end='2035-12-01')
    ci = forecast.conf_int()

    forecasted.append(forecast.predicted_mean)
    forecasts = pd.DataFrame(forecasted).T
    forecasts = forecasts.rename(columns={'predicted_mean': 'value'})
    real = pd.DataFrame(X)
    real = real.rename(columns={'ALLSKY_KT': 'value'})
    results = pd.concat([real, forecasts])
    results = results.rename(columns={'value': 'solar'})
    return results
