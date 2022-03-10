import pandas as pd
import numpy as np


def arima_averages(df):
    allSolar = df['Solar Ratio'].tolist()

    avgSolar = []
    years = []

    month = 0
    sum = 0
    year = 1984

    for x in allSolar:
        sum += x
        month += 1
        if month == 12:
            avgSolar.append(sum/12)
            years.append(year)
            year += 1
            month = 0
            sum = 0

    avg = pd.DataFrame()
    avg['Solar Ratio'] = avgSolar
    avg['Year'] = years
    return avg
