import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, ExtraTreeRegressor

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression, LassoCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor

import matplotlib.pyplot as plt

import statsmodels.api as sm

data = pd.read_csv('ds_2.csv')

#data = data[data['F1'] == 3]

X = data[['F1', 'F2',  'F4', 'F3']]
y = data['Avg']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1111)

model = sm.OLS(y, X).fit()
#predictions = model.predict(X)

print(model.summary())


for degree in range(1, 8):
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    #print(model.steps[1][1].coef_)
    print(score)