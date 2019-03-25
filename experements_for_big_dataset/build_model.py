import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, ExtraTreeRegressor

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor

import matplotlib.pyplot as plt

data = pd.read_csv('dataset_big.csv')

data = data[data['F1'] == 8]
X = data[['F1', 'Avg']]
y = data['F5']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1111)


model = ExtraTreeRegressor(max_depth=8)
model.fit(X_train, y_train)
score = model.score(X_test, y_test)

print(score)
neural_net = MLPRegressor(max_iter=200).fit(X_train, y_train)
print(neural_net.score(X_test, y_test))

fig, ax = plt.subplots()
ax.scatter( data['F4'], data['Avg'])
plt.show()


for degree in range(10):
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    print(score)
