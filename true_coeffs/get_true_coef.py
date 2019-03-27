import math
import pandas as pd

def get_t_s():
    data =pd.read_csv('ds_2.csv')
    data['Square_1'] = (data['Ex1'] - data['Avg'])**2
    data['Square_2'] = (data['Ex2'] - data['Avg'])**2
    data['Square_3'] = (data['Ex3'] - data['Avg'])**2

    data['S_squared'] = data[['Square_1', 'Square_2', 'Square_3']].sum(axis=1) / (len(data) * 2)

    s_squared_sum = data['S_squared'].sum(axis=0)
    s_squared_sum_y = s_squared_sum / len(data)
    s_coeff = math.sqrt(s_squared_sum_y/(len(data) * 2))
    print(s_coeff)
    t = 1.9612

    t_s = t * s_coeff

    return t_s