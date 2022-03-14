# SERF: Solar Energy Resource Forecasting
## Motivation
Transitioning to renewable energy resources is key to mitigating the effects of climate change. 
For companies and individuals interested in switching to renewable energy resources, it is important to know whether those resources will be reliable in the future. In this package, we’ve forecasted the solar resource (i.e. solar irradiance) based upon prior historical data for the purpose of understanding how solar irradiance may change over time and which locations across Washington State are optimal for said resource. This model may be used for other locations and for forecasting other renewable energy resources if so desired in the future. 

## Methods
A commonly used statistical method for time series forecasting is the ARIMA model.
Autoregressive integrated moving average, or ARIMA, Utilizes lagged values (autoregressive) of a target variable to make a prediction based on trends (integrated). The model also takes lagged prediction errors as inputs (moving average) to improve prediction accuracy.

This program utilizes SARIMA (seasonal auto-regressive integrated moving average) which is an extension of the statistical prediction approach ARIMA. SARIMA handles univariate time series data with seasonal variations. For this package, the model takes in historical irradiance data for specific geolocations in a confined geographical region. and predicts future irradiance data for each of the geolocations. The prediction data for each of the locations is then used to provide estimates (based on a linear surface fit) for locations that lie between the known locations.

## Usage
Provide an example of how to use the software

## License 
Our project is licensed under the MIT license. See ``LICENSE`` for more information.

## Acknowledgments
The Prediction of Worldwide Energy Resource (POWER) Project is funded through the National Aeronautics and Space Administration (NASA) Applied Sciences Program within the Earth Science Division of the Science Mission Directorate. The POWER team could not have completed this task without both technical and scientific inputs from the following Earth Science Division teams: The World Climate Research Programme (WCRP) Global Energy and Water Cycle Experiment's (GEWEX) Surface Radiation Budget (SRB) and the Clouds and the Earth's Radiant Energy System (CERES) projects at NASA LaRC and the Global Modeling and Assimilation Office at the NASA Goddard Space Flight Center. The data obtained through the POWER web services was made possible with collaboration from the NASA Langley Research Center (LaRC) Atmospheric Science Data Center (ASDC).

## Contact Information
Claire Benstead
Spencer Cira
Isabelle Pacheco
Erick Tieu
