### Explanation of the functions used to process the raw geojson

The following functions, which can be found in the ``json_to_csv.py`` process the data received from NASA POWER Project in geojson format. 

``
import geopandas as gp
import pandas as pd
import datetime as dt
import numpy as np
import os``


### Import

``import_geojson`` accepts the geojson filepath and reads with geopandas. The datasets for this project were stored in a sub-directory named ``NASA``. Errors will raise if the file format is not .json or if the input parameter is not a string.

``
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
`` 

### Convert

``convert_data`` accepts the return of the ``import_geojson`` function and extracts the dataset from the .json file. The data is converted to a pandas DataFrame. 

``
def convert_data(data):
    '''converts parameter column to dict then df reads with Pandas'''
    data_dict = data['parameter'][0]
    pd_df = pd.DataFrame.from_dict(data_dict)
    df = pd.DataFrame(pd_df)
    return(df)
``

### Clean up dataset

The datasets we used contained both monthly and yearly averaged, indexed in YYYYMM format, with the yearly average listed as the 13th month. In order to use the data in SARIMAX, the yearly averages were removed using the ``remove_annual`` function. 

With the yearly averages removed, the length of each dataset was 444 rows. A ValueError will raise if the returned dataframe is not 444 rows. This can be manually edited or removed if the dataset is a different length.

``
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
``
### Convert index to Datetime

SARIMAX infers frequency based on index frequency. For a monthly frequency to be inferred correctly, the ``to_datetime`` function converts the YYYYMM index to YYYY-MM-DD Datetime format. 

``
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
``

### Compiled Function
``geojson_to_csv`` contains all four previous functions into one for ease of use.

``
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
`` 