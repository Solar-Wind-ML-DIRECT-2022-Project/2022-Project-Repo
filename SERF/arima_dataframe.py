import pandas as pd
import datetime as dt


def arima_results(pred_sol):
    df = pd.DataFrame()
    df['Solar Ratio'] = pred_sol
    # Associating a year and a month with the ARIMA predictions
    years = []
    year = 1984
    month = 1
    day = 1
    # Only works for predictions from 0 to 601
    for x in range(601):
        if month == 12:
            year += 1
            month = 1
        years.append(datetime.date(year, month, day))
        month += 1
    # Adding the time column 'Year' to the ARIMA dataframe
    df['Year'] = years
    return df
