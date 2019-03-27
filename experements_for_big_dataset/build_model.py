import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression

import statsmodels.api as sm

from true_coeffs.get_true_coef import get_t_s

data = pd.read_csv('ds_2.csv')


X = data[['F1', 'F2', 'F3', 'F4']]
y = data['Avg']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1111)

model = sm.OLS(y, X).fit()

print(model.summary())


for degree in range(1, 8):
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    #print(model.steps[1][1].coef_)
    print(score)
model = make_pipeline(PolynomialFeatures(4), LinearRegression())
model.fit(X_train, y_train)
score = model.score(X_test, y_test)
model_coeffs = model.steps[1][1].coef_
model_inter = model.steps[1][1].intercept_
features = model.steps[0][1].get_feature_names(['F1', 'F2', 'F3', 'F4'])
print(score)
print('inter', model_inter)
t = get_t_s()
print(t)
features_dict = {}
ans_str = str(model_inter)
for feature, coef in zip(features, model_coeffs):
    if abs(coef) > t:
        features_dict[feature.replace(' ', '*').replace('^', '**')] = coef

for k, v in features_dict.items():
    plus = ''
    if v > 0:
        plus = '+'
    ans_str += plus + '{:.2e}'.format(v) + '*' + k
print(ans_str)
