import random as r
import numpy as np
from main_tools import GeneticAlg
from transfer_to_bits import opt, transform_params, full_choice_smart

exp_res_dict = {}
class Block:
    def __init__(self, name, prop_1, prop_2, prop_3, prop_4, prop_5, min_blocks, max_blocks):
        self.name = name
        self.prop_1 = prop_1
        self.prop_2 = prop_2
        self.prop_3 = prop_3
        self.prop_4 = prop_4
        self.prop_5 = prop_5
        self.min_blocks = min_blocks
        self.max_blocks = max_blocks

rangs = {
    'prop_1': [0.25, 1],
    'prop_2': [0.3,  1],
    'prop_3': [0.2, -1],
    'prop_4': [0.15, -1],
    'prop_5': [0.1, 1]
}

ga_params = {
    'population': range(10, 20),
    'generations': range(10, 20),
    'cross_chance': np.arange(0.1, 0.95, 0.05),
    'mut_chance': np.arange(0.1, 0.95, 0.05)
}


RG = Block('РГ',        200, 5, 30, 600,    2400,   1, 10)
IPSM = Block('ИПСМ',    210, 4, 30, 600,    2600,   1, 10)
KVS = Block('КВС',      190, 4, 40, 700,    2000,   1, 10)
ZIV = Block('ЗИВ',      200, 5, 30, 600,    2300,   1, 10)
FTS = Block('ФТС',      180, 5, 30, 600,    2500,   1, 10)
KG_SV = Block('КГ-СВ',  200, 5, 30, 600,    2400,   1, 10)
PPK = Block('ППК',      205, 4, 30, 600,    2400,   1, 10)

results = {}


#первый эксеремент
total_case = 15
all_blocks = [RG, IPSM, KVS, ZIV, FTS, KG_SV]

optimum = opt(rangs)
blocks = transform_params(all_blocks)
full_choice_result = full_choice_smart(blocks, total_case, optimum, rangs)[1]

for exp in range(2):
    exp_points = [r.choice(ga_params['population']), r.choice(ga_params['generations']), round(r.choice(ga_params['cross_chance']), 2), round(r.choice(ga_params['mut_chance']), 2)]
    GA = GeneticAlg(blocks, total_case, optimum, rangs, exp_points[0], exp_points[1], exp_points[2], exp_points[3])
    print([3] + exp_points)
    exp_key = tuple([3] + exp_points)
    results[exp_key] = []

    for i in range(3):  # 3 эксперемента для каждого
        results_for_10_starts = []
        for pusk in range(10):  # 10 запусков алгоритма
            result_for_10_starts = GA.start()
            results_for_10_starts.append(result_for_10_starts[0][1])
        ga_result = np.array(results_for_10_starts).mean() - full_choice_result
        results[exp_key].append(ga_result)
    results[exp_key].append(np.array(results[exp_key]).mean())

print(results)




