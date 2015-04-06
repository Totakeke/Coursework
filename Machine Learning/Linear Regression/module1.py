import pandas as pd
import numpy as np
import statsmodels.api as sm

x_data = pd.read_csv('X.txt', names=['intercept term','number of cylinders','displacement','horsepower','weight','acceleration','model year'])
y_data = pd.read_csv('Y.txt', names=['mpg'])

est = sm.OLS(y_data, x_data).fit()
est.summary()