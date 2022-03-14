<p align="center">
    // ![alt text](https://github.com/Solar-Wind-ML-DIRECT-2022-Project/2022-Project-Repo/blob/main/serf/serf%20logo.png "SERF logo")
</p>

# SERF: Solar Energy Resource Forecasting 
---
## Motivation
The future of energy is renewable.

Though this has long been the leading sentiment regarding climate change, global warming, and the future of the earth and humanity alike, there are still many logistical questions that need to be answered before transitioning to renewable energy resources can become mainstream. Many homeowners are hesitant to rely on “unreliable” resources like sunlight and wind power, given the unpredictable nature of nature itself. And in temperate climates like Washington, where the sun all but disappears during the winter, investing in solar panels—for both individual consumers and companies alike—seems like a high risk, low reward gamble.

The Solar Energy Resource Forecasting (SERF) project aims to address concerns about the future of solar energy in a climate that grows more unpredictable with climate change every year. Drawing from historical trends in solar irradiance, using data provided by NASA’s POWER project (see: Acknowledgements), we introduce a forecasting tool for companies and individuals to use to plan their investment in solar energy with more confidence. Created with the state of Washington in mind, our model forecasts solar resource availability based on geographic location through 2035. 


## Methods
A commonly used statistical method for time series forecasting is the ARIMA model. Autoregressive integrated moving average, or ARIMA, Utilizes lagged values (autoregressive) of a target variable to make a prediction based on trends (integrated). The model also takes lagged prediction errors as inputs (moving average) to improve prediction accuracy.

This package utilizes SARIMA (seasonal auto-regressive integrated moving average) which is an extension of the statistical prediction approach ARIMA. SARIMA handles univariate time series data with seasonal variations. For this package, the model takes in historical irradiance data for specific geolocations in a confined geographical region and predicts future irradiance data for each of the geolocations. The prediction data for each of the locations is then used to provide estimates (based on a linear surface fit) for locations that lie between the known locations.

## Usage
Provide an example of how to use the software

## License 
Our project is licensed under the MIT license. See ``LICENSE`` for more information.

## Acknowledgments
The Prediction of Worldwide Energy Resource (POWER) Project is funded through the National Aeronautics and Space Administration (NASA) Applied Sciences Program within the Earth Science Division of the Science Mission Directorate. The POWER team could not have completed this task without both technical and scientific inputs from the following Earth Science Division teams: The World Climate Research Programme (WCRP) Global Energy and Water Cycle Experiment's (GEWEX) Surface Radiation Budget (SRB) and the Clouds and the Earth's Radiant Energy System (CERES) projects at NASA LaRC and the Global Modeling and Assimilation Office at the NASA Goddard Space Flight Center. The data obtained through the POWER web services was made possible with collaboration from the NASA Langley Research Center (LaRC) Atmospheric Science Data Center (ASDC).

## Contact Information
Claire Benstead - cbens01@uw.edu    <br>
Spencer Cira - sgcira@uw.edu  <br>
Isabelle Pacheco - ipach@uw.edu   <br>
Erick Tieu - etieu@uw.edu    <br>
