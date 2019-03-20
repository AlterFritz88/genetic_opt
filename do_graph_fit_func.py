import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

from transfer_to_bits import *

KVS = Block('КВС',  10, 1,   1, 10)
RG = Block('РГ',    6, 4,   1, 10)

all_blocks = [KVS, RG]

rangs = {
    'cost': [0.2, -1],
    'wires': [0.25, 1],
    'cost1': [0.25, +1],
    'wires1': [0.3, -1],
    #  'power':        [0.1, 1],
    #  'russian_mc':   [0.1, -1],
    #  'time_to_build':[0.1, -1],
    #  'count_elem':   [0.5, -1]
}
total_case = 20
optimum = opt(rangs)

transformed_blocks = transform_params(all_blocks)


full_choice_ans = full_choice(transformed_blocks, total_case, optimum, rangs)

X = np.array([int(x[0].split(' ')[0]) for x in full_choice_ans])
Y = np.array([int(x[0].split(' ')[1]) for x in full_choice_ans])
Z = np.array([x[1] for x in full_choice_ans])



fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(X, Y, Z, c=Z, cmap='hot', linewidth=3)
plt.xlabel('Кол-во блоков КВС шт.')
plt.ylabel('Кол-во блоков РГ шт.')
plt.title('Зависимость значения функции приспособленности от количесва блоков в системе')
ax.set_zlabel('Значение fit functon')

plt.show()