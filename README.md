![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Solar-Wind-ML-DIRECT-2022-Project/2022-Project-Repo)
![GitHub contributors](https://img.shields.io/github/contributors-anon/Solar-Wind-ML-DIRECT-2022-Project/2022-Project-Repo)
![GitHub last commit](https://img.shields.io/github/last-commit/Solar-Wind-ML-DIRECT-2022-Project/2022-Project-Repo)
![GitHub](https://img.shields.io/github/license/Solar-Wind-ML-DIRECT-2022-Project/2022-Project-Repo)
<p align="center">
  <img width="300" height="260" src="https://github.com/Solar-Wind-ML-DIRECT-2022-Project/2022-Project-Repo/blob/main/serf/serf%20logo.png">
</p>

# SERF: Solar Energy Resource Forecasting 

## Motivation
The future of energy is renewable.

Though this has long been the leading sentiment regarding climate change, global warming, and the future of the earth and humanity alike, there are still many logistical questions that need to be answered before transitioning to renewable energy resources can become mainstream. Many homeowners are hesitant to rely on “unreliable” resources like sunlight and wind power, given the unpredictable nature of nature itself. And in temperate climates like Washington, where the sun all but disappears during the winter, investing in solar panels—for both individual consumers and companies alike—seems like a high risk, low reward gamble.

The Solar Energy Resource Forecasting (SERF) project aims to address concerns about the future of solar energy in a climate that grows more unpredictable with climate change every year. Drawing from historical trends in solar irradiance, using data provided by NASA’s POWER project (see: Acknowledgements), we introduce a forecasting tool for companies and individuals to use to plan their investment in solar energy with more confidence. Created with the state of Washington in mind, our model forecasts solar resource availability based on geographic location through 2035. 


## SARIMA: the model
A commonly used statistical method for time series forecasting is the autoregressive integrated moving average, or ARIMA, model. This supervised learning model utilizes lagged values (autoregressive) of a target (endogenous) variable to make a prediction based on trends (integrated). The model also accepts lagged prediction errors as inputs (moving average) to improve prediction accuracy.

SERF utilizes SARIMA (seasonal auto-regressive integrated moving average) which is an extension of the statistical prediction approach ARIMA. SARIMA handles univariate time series data with seasonal variations. For this package, the model is fitted to historical solar irradiance index for specific geolocations in a confined geographical region (Washington) and forecasts future location-specific irradiance monthly averages. These forecasted averages are then used to provide estimates (based on a linear surface fit) for locations that lie between the known locations.

### Hyperparameters
The hyperparameters present in the SARIMA model are p, d, q for the ARIMA component and P, D, Q, s for the seasonal component. Parameters p and P correspond to the order of the autoregressive (AR) term. Parameters d and D correspond to the differencing of the data or the (I) term. Parameters q and Q correspond to the moving average (MA) term. Parameter s is the seasonal term, and in the case of solar forecasting is equal to 12, following the yearly cycle of solar insolence.<br><br>
To optimize these parameters, rather than treating them as derived values, they were optimized to best fit the data. This was performed by splitting the whole dataset into a training set, a validation set, and a testing set. The testing set contains the last 4 years of data. The validation set contains the previous 4 years from the testing set. The training set contains the remaining data. The model was then trained on the training set and a Tree-structures Parzen Estimator (TPE) algorithm was used to find the best performing set of hyperparameters. Model accuracy was calculated by predicting the values of validation set and evaluating the error by calculating the r^2 value. 50 runs of the TPE sampler was used for each location. The hyperparameters were bounded by (8,1,8)x(3,1,3,s) for (p,d,q)x(P,D,Q,s), which was determined by running an optimization at a single location with a broader range and observing the bounds of the hyperparameters.<br><br>
The resulting optimized hyperparameters are then used to evaluate the testing set and are used in the final model.<br><br>  

### Using SARIMAX

Though the SERF package has been specifically tailored to Washington-area datasets from NASA dated from 1984-2020, the backbone of the python code and functions could be applied to other regions, other target variables, or different forecasting periods. 

The forecasting model used in this package is SARIMAX, or SARIMA with Exogenous variables. This model allows for multivariate predictions, in the case that additional exogenous variables affect the behavior of the target variable. The drawback to this model exists with forecasting, as any out-of-sample forecasting still requires existent exogenous data. For this reason, we were unable to apply the multivariate aspect to our package, but it may be useful in other cases. 

See the ``examples`` directory for explanations and examples of the package functions, and how they could be modified for future use.

## Usage

### Requirements

The SERF package uses the following main dependency:

1. Python 3.7

A detailed list of dependencies can be accessed in ``environment.yml``. 

### Cloning and Installation

Step 1: The SERF package can be accessed via the Github repo. To clone: ``git clone https://github.com/Solar-Wind-ML-DIRECT-2022-Project/2022-Project-Repo.git``. <br>
Step 2: Install the environment necessary to run the software. To create the environment: ``conda env create -f environment.yml``. <br>
Step 3: Open ``Plotly Updated.ipynb``. To open: ``jupyter notebook 'Plotly Updated.ipynb'``. <br>
Step 4: Interact with the code via ``Plotly Updated.ipynb``, simply run each cell block and interact with the plots as you wish.

### Interacting with Plotly
As mentioned above, once the ``Plotly Updated.ipynb`` is opened on your local computer, the cells can simply be run to visualize the analysis. Below are some examples of the functionality and visualization capabilities currently available within the software.

#### Map of all the locations in the database
![GitHub code size in bytes](https://github.com/Solar-Wind-ML-DIRECT-2022-Project/2022-Project-Repo/blob/main/serf/Map.png)
<p align="center">
  

#### Forecast for a single location
![GitHub code size in bytes](https://github.com/Solar-Wind-ML-DIRECT-2022-Project/2022-Project-Repo/blob/main/serf/example%20plots/Kennewick%20yearly%20avg%20line%20plot.png)
<p align="center">


#### Forecast for all locations
![GitHub code size in bytes](https://github.com/Solar-Wind-ML-DIRECT-2022-Project/2022-Project-Repo/blob/main/serf/example%20plots/All%20locations%20yearly%20avg%20line%20plot.png)
<p align="center">


## Organization
Univeristy of Washington, Department of Chemical Engineering <br>
3781 Okanogan Ln, Seattle, WA 98105


## License 
Our project is licensed under the MIT license. See ``LICENSE`` for more information.


## Acknowledgments

<p align="center">
  <img width="260" height="100" src="https://power.larc.nasa.gov/docs/gallery/images/power_logo.png">
</p>

These data were obtained from the NASA Langley Research Center (LaRC) POWER Project funded through the NASA Earth Science/Applied Science Program.

The Prediction of Worldwide Energy Resource (POWER) Project is funded through the National Aeronautics and Space Administration (NASA) Applied Sciences Program within the Earth Science Division of the Science Mission Directorate. The POWER team could not have completed this task without both technical and scientific inputs from the following Earth Science Division teams: The World Climate Research Programme (WCRP) Global Energy and Water Cycle Experiment's (GEWEX) Surface Radiation Budget (SRB) and the Clouds and the Earth's Radiant Energy System (CERES) projects at NASA LaRC and the Global Modeling and Assimilation Office at the NASA Goddard Space Flight Center. The data obtained through the POWER web services was made possible with collaboration from the NASA Langley Research Center (LaRC) Atmospheric Science Data Center (ASDC).


## Contact Information
Claire Benstead - cbens01@uw.edu    <br>
Spencer Cira - sgcira@uw.edu  <br>
Isabelle Pacheco - ipach@uw.edu   <br>
Erick Tieu - etieu@uw.edu    <br>


