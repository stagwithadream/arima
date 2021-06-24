import pandas as pd
from datetime import datetime


import warnings
from pandas import read_csv
from pandas import datetime
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

dataset=pd.read_csv("C:\\Users\Sairam Reddy\Desktop\ARIMA\scrapped datasets\completeValues\hyd_So2_pollution_data_completeValues.csv")
#print(dataset)
dataset['Date']=pd.to_datetime(dataset['Date'],infer_datetime_format=True)
#print(dataset.values)
indexedDataset=dataset.set_index(['Date'])    
df = indexedDataset.copy()
print(indexedDataset.values)




# evaluate an ARIMA model for a given order (p,d,q)
def evaluate_arima_model(X, arima_order):
    # prepare training dataset
    train_size = int(len(X) * 0.66)
    train, test = X[0:train_size], X[train_size:]
    history = [x for x in train]
    # make predictions
    predictions = list()
    for t in range(len(test)):
        model = ARIMA(history, order=arima_order)
        model_fit = model.fit(disp=0)
        yhat = model_fit.forecast()[0]
        predictions.append(yhat)
        history.append(test[t])
    # calculate out of sample error
    error = mean_squared_error(test, predictions)
    return error

print(evaluate_arima_model(indexedDataset.values,(1,1,1)))


