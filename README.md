# SERF: Solar Energy Resource Forecasting
## Motivation
This package is intended to forecast the solar resource (i.e. solar irradiance) based on prior historical data for a variety of locations across Washington State.

## Methods
This program utilizes SARIMA (seasonal auto-regressive integrated moving average) which is a an extension of the statistical predicition approach ARIMA (autoregressive integrated moving average). SARIMA handles univariate time series data that has seasonal variations. The software takes in historical irradiance data for specific geolocations in a confined geographical region. With this data, SARIMA predicts future irradiance data for each of the geolocations. The prediction data for each of the locations is then used to provide estimates (based on a linear surface fit) for locaitons that lie between the known locations.

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
