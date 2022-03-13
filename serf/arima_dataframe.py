import pandas as pd
import datetime

# pred_sol was a list that was the prediction from ARIMA
def arima_results(df):
    # Associating a year and a month with the ARIMA predictions
    df = df.rename(columns = {"solar": "Solar Ratio"})
    years = []
    year = 1984
    month = 1
    day = 1
    # Only works for predictions from 0 to 624
    for x in range(624):
        if month == 13:
            year += 1
            month = 1
        years.append(datetime.datetime(year, month, day))
        month += 1
    # Adding the time column 'Year' to the ARIMA dataframe
    df['Year'] = years
    return df
