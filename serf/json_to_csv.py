import geopandas as gp
import pandas as pd
import datetime as dt
import numpy as np
import os


def import_geojson(geojson):
    '''imports geojson to notebook and reads with geopandas'''
    '''input must be in 'NASA/<file.json>' format, or other path name'''
    filename = geojson
    
    if type(filename) == str:
        pass
    else:
        raise TypeError('input is not a string')
        return

    if os.path.exists(geojson):
        pass
    else:
        raise ValueError('file does not exist')
    
    if filename.endswith('.json'):
        data = gp.read_file(filename)
    else:
        raise TypeError('file extension is not .json.')
    return(data)


def convert_data(data):
    '''converts parameter column to dict then df reads with Pandas'''
    data_dict = data['parameter'][0]
    pd_df = pd.DataFrame.from_dict(data_dict)
    df = pd.DataFrame(pd_df)
    return(df)


def remove_annual(df):
    '''remove the annual average rows (13th month) from df'''
    monthly = df[~df.index.str.endswith('13', na=False)]
    if len(monthly) > 444:
        raise ValueError('Check length of dataset.')
    elif len(monthly) < 444:
        raise ValueError('Check index. Length of dataset is short.')
    else:
        pass
    return(monthly)


def to_datetime(monthly):
    '''convert index from yearmonth string to datetime'''
    def append(dfseries):
        dfseries = dfseries[:4] + '-' + dfseries[4:]
        return dfseries

    monthly.index = monthly.index.rename('ds')
    dated = monthly.reset_index()
    dated['ds'] = dated['ds'].apply(append)
    dated = dated.set_index('ds')
    dated.index = pd.to_datetime(dated.index)
    return(dated)


def geojson_to_csv(geojson):
    '''convert geojson to csv'''
    '''input must be in 'NASA/<file.json>' format, or other path name'''
    data = import_geojson(geojson)
    df1 = convert_data(data)
    monthly = remove_annual(df1)
    df = to_datetime(monthly)
    if not isinstance(df.index, pd.core.indexes.datetimes.DatetimeIndex):
        raise TypeError('index type must be DatetimeIndex')
    else:
        pass
    return(df)
