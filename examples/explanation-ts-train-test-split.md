## Explanation of train-test split functions

Given the time-sensitive nature of the data, a time series train-test split is used in place of a randomized train-test split.


    import numpy as np
    import geopandas as gp
    import pandas as pd

    import datetime as dt

    import json_to_csv

Using the pandas dataframe created with the ``geojson_to_csv`` function, ``uni_selection`` function extracts the ``ALLSKY_KT`` column and creates a new, simplified dataframe. ``ALLSKY_KT`` was the All Sky Insolation Clearness Index, and this can be modified in the code to select any other variable of choice. 

    def uni_selection(df, variable=['ALLSKY_KT']):
        '''for univariate SARIMAX model, creates a new df with solar index'''
        X = df[variable]
        if type(X) != pd.DataFrame:
            raise TypeError('X is pd.Series, not DataFrame. Check parameters.')
        else:
            pass
        return(X)

With the dataframe returned in the previous function, ``single_split`` performs a time-series split on the dataset. The default test size is set to 48 months (four years), but this can be changed to a different value. 

*The sample size must be a positive integer. A negative sample size will create a test set from the beginning of the dataset, aka starting in 1984.*

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
