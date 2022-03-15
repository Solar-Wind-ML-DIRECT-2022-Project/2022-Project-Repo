## Explanation of the function in forecast_single.py

This function requires a pandas df with metadata for all locations. Optimized hyperparamater values and filepath are required, but MSE and r2 scores are not. 

``forecast`` accepts a single location input, specified by the row index (sample) in the dataframe (locations). It uses the optimized hyperparameters to define the SARIMAX model and fits it to the entire available dataset (in this case, 1984-01-01 to 2020-12-01). Using the parameters from the fitted model, the function forecasts out to 2035-12-01 using ``get_prediction``. The function returns a single-column pandas dataframe with all historical values and all forecasted values concatenated together.

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
        model = SARIMAX(X, order=(p, d, q), seasonal_order=(P, D, Q, s),
                        enforce_stationarity=False, enforce_invertibility=False)
        fit_model = model.fit(maxiter=50, method='powell', disp=False)
        forecast = fit_model.get_prediction(start='2021-01-01', end='2035-12-01')
        # ci = forecast.conf_int()

        forecasted.append(forecast.predicted_mean)
        forecasts = pd.DataFrame(forecasted).T
        forecasts = forecasts.rename(columns={'predicted_mean': 'value'})
        real = pd.DataFrame(X)
        real = real.rename(columns={'ALLSKY_KT': 'value'})
        results = pd.concat([real, forecasts])
        results = results.rename(columns={'value': 'solar'})
        return results

The ``get_prediction`` function from statsmodels was used instead of ``forecast`` or ``get_forecast`` because it allows for both in-sample predictions and out-of-sample foecasting, with higher specificity . This function was written to start forecasting on 2021-01-01 and end on 2035-12-01, and these dates could be modified if desired. ``get_prediction`` also allows for dynamic predictions, so in-sample forecasting is possible without using a train-test split.

Confidence intervals can also be obtained using ``get_prediction``, and was written into this ``forecast`` function as an optional return. The function can be modified to return confidence intervals if so desired.