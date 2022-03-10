__version__ = "1.0"

# optimizing hyperparameters

import geopandas as gp
import pandas as pd
import optuna
import numpy as np
import sklearn

from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import r2_score
from statsmodels.tsa.statespace.sarimax import SARIMAX

def loadjson(filename, column_name='ALLSKY_KT'):
    geodf = gp.read_file(filename)
    Idict = geodf['parameter'][0]
    Idf =  pd.DataFrame.from_dict(Idict)
    df = pd.DataFrame(Idf[column_name])
    return df

def rm13(df):
    """
    remove every 13th row to get rid of yearly average in geojson files.
    """
    df = df.drop(df.index[12::13])
    return df

def numtodate(dfseries):
    dfseries = dfseries[:4] + '/' + dfseries[4:]
    return dfseries

def Prophet_preproc(df, column_y="ALLSKY_KT"):
    df = df.rename(columns={column_y: "y"})
    df['ds'] = df.index
    df['ds'] = df['ds'].astype(str)
    df['ds'] = df['ds'].apply(numtodate)
    return df

def TSS(df):
    X = df['ds'].values
    y = df['y'].values
    X_dict = {}
    y_dict = {}
    kmax = 11
    tss = TimeSeriesSplit(gap=0, max_train_size=None, n_splits=kmax)
    k=0
    for train_index, test_index in tss.split(X):
        X_dev, X_test = X[train_index], X[test_index]
        y_dev, y_test = y[train_index], y[test_index]
        if k == kmax-2:
            X_train, X_val = X[train_index], X[test_index]
            y_train, y_val = y[train_index], y[test_index]
        k=k+1

    X_dict['X_dev'] = X_dev
    X_dict['X_test'] = X_test
    X_dict['X_train'] = X_train
    X_dict['X_val'] = X_val

    y_dict['y_dev'] = y_dev
    y_dict['y_test'] = y_test
    y_dict['y_train'] = y_train
    y_dict['y_val'] = y_val

    return(X_dict,y_dict)

def r2score_TSS(train_data,val_data,p,d,q,P,D,Q):
    model = SARIMAX(train_data, order=(p, d, q),seasonal_order=(P, D, Q, 12),
                 enforce_stationarity=False, enforce_invertibility=False)
    model_fit = model.fit(maxiter=50, method='powell')

#   start and end value is data dependent    
    y_pred = model_fit.predict(start = 370, end = 406)
    score = r2_score(val_data, y_pred)
    return score

def objective(trial,y_train,y_val):
    # define hyperparameter space
    p = trial.suggest_int("p", 0, 8)
    d = trial.suggest_int("d", 0, 1)
    q = trial.suggest_int("q", 0, 8)
    P = trial.suggest_int("P", 0, 3)
    D = trial.suggest_int("D", 0, 1)
    Q = trial.suggest_int("Q", 0, 3)
    
    # get the score for the hyperparameters chosen
    score = r2score_TSS(y_train,y_val,p,d,q,P,D,Q)
    
    return score

def study_hyper(y_train,y_val):

    argfunction = lambda trial: objective(trial,y_train,y_val)
    study = optuna.create_study(
        sampler=optuna.samplers.TPESampler(), direction='maximize')
    study.optimize(argfunction, n_trials=50)
        #,y_train=y_train,y_val=y_val)

    results = study.trials_dataframe()
    return results

def resultstocsv(results):
    results.to_csv('../../SARIMAX_hyperparameter_results.csv') 
    return results

