# RennesDataChallenge 2024

This repositery was created for the Rennes Data Challenge 2024. The goal was to predict the value of crypto-currencies on a day-to-day basis. 

Since then, this reposity have been frequently updated to implement new models and improve existing one.

## About data 

The dataset is a time series at business days frequency between 08-2017 and 03-2023. This dataset contains 200 columns: economic variables, social networks (number of tweets about BTC, sentiment of tweets), etc...

## Models

- Baseline : provide a naive forecasting method by using the previous value of the time series as the prediction of the next value
- Linear regression
- Facebook Prophet
- RandomForests
- XGBoost
- LSTM

## Preprocessing pipeline 

**Missing data** : 
1. removing columns with more than *x*% of missing values
2. imputing missing values with the *KNNImputer()*

**Scaling data** : *RobustScaler()* is used. It natively provide a way to deal with outliers by scaling features according to the IQR.

**Features extraction** :
1. **Lag features** : the previous *x* values of the time series
2. **Rolling statistics** : the mean and the standard deviation of the time series over the last *x* days
3. **Day of the week** : angular distance of encoded day of the week

Note : Bitcoin price doesn't have a strong weekly or monthly seasonality (see EDA). However day of the week is taken into account here as data frequency is business days and although no weekly seasonality have been observed we could assume exogenous features may be affected by weekends gaps.


**Dimensionality reduction** : Here two options are available and will be tested
1. **PCA** : reduce dimensionality by mapping linear relation of features
2. **Autoencoder** : gives the ability to interpolate non linear relation between features

### Model evaluation and parameter tuning

We first divide the dataset into 3 sets :
1. **Training set** : used to train the model
2. **Validation set** : used to tune the model's hyperparameters
3. **Test set** : used to evaluate the model's performance

Once validation set have been used to find the best hyperparameters, we can finally train a model training + validation set.

### Backtesting strategy

In order to achieve best performance, we can use a backtesting strategy to improve the model's performance. The idea is that through each new day we can retrain the model with the most recent data and predict the next day's value. This way we can take into account the most recent information and improve the model's performance.

![Backtesting strategy](figures/single_step_refit.gif)