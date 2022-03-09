import geopandas as gp
import pandas as pd
import datetime as dt
import numpy as np

def import_geojson(geojson):
    '''imports geojson to notebook and reads with geopandas'''
    '''input must be in 'NASA/<file.json>' format, or other path name'''
    filename = geojson
    data = gp.read_file(filename)
    return(data)

def convert_data(data):
    '''converts parameter column to dict then df reads with Pandas'''
    data_dict = data['parameter'][0]
    pd_df = pd.DataFrame.from_dict(data_dict)
    df = pd.DataFrame(pd_df)
    return(df)

def remove_annual(df):
    '''remove the annual average rows (13th row) from df'''
    monthly = df.drop(df.index[12::13])
    return(monthly)

def to_datetime(monthly):
    '''convert index from yearmonth string to datetime'''
    def append(dfseries):
        dfseries = dfseries[:4] + '-' + dfseries[4:]
        return dfseries

    monthly['ds']= monthly.index
    monthly['ds'] = monthly['ds'].apply(append)
    
    monthly['Year']= monthly.index
    monthly['Year'] = pd.to_datetime(monthly['ds'])
    return(monthly)

def geojson_to_csv(geojson):
    '''convert geojson to csv'''
    '''input must be in 'NASA/<file.json>' format, or other path name'''
    data = import_geojson(geojson)
    df1 = convert_data(data)
    monthly = remove_annual(df1)
    df = to_datetime(monthly)
    return(df)