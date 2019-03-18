import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

from transfer_to_bits import *

KVS = Block('КВС',  10, 1,   1, 8)
RG = Block('РГ',    6, 4,   1, 8)

all_blocks = [KVS, RG]

rangs = {
    'cost': [0.4, -1],
    'wires': [0.6, 1],
    #  'power':        [0.1, 1],
    #  'russian_mc':   [0.1, -1],
    #  'time_to_build':[0.1, -1],
    #  'count_elem':   [0.5, -1]
}
total_case = 12
optimum = opt(rangs)

transformed_blocks = transform_params(all_blocks)


full_choice = {}
for kg in range(1, 9):
    for kvs in range(1, 9):

        if sum([kg, kvs]) > total_case:
            continue
        temp_list = [str(kg), str(kvs)]
        full_choice[' '.join(temp_list)] = func_opt([kg, kvs], transformed_blocks, optimum)

full_choice_sorted = sorted(full_choice.items(), key=lambda kv: kv[1])
print(full_choice_sorted)

X = np.array([int(x[0].split(' ')[0]) for x in full_choice_sorted])
Y = np.array([int(x[0].split(' ')[1]) for x in full_choice_sorted])
Z = np.array([x[1] for x in full_choice_sorted])



fig = plt.figure()
ax = plt.axes(projection='3d')
ax.scatter(X, Y, Z, c=Z, cmap='hot', linewidth=3)
plt.xlabel('Кол-во блоков КВС шт.')
plt.ylabel('Кол-во блоков РГ шт.')
plt.title('Зависимость значения функции приспособленности от количесва блоков в системе')
ax.set_zlabel('Значение fit functon')

plt.show()