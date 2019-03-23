from itertools import product
import numpy as np

from main_tools import GeneticAlg
from transfer_to_bits import opt, transform_params, full_choice, full_choice_smart

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

RG = Block('РГ',        200, 5, 30, 600,    2400,   1, 10)
IPSM = Block('ИПСМ',    210, 4, 30, 600,    2600,   1, 10)
KVS = Block('КВС',      190, 4, 40, 700,    2000,   1, 10)
ZIV = Block('ЗИВ',      200, 5, 30, 600,    2300,   1, 10)
FTS = Block('ФТС',      180, 5, 30, 600,    2500,   1, 10)
KG_SV = Block('КГ-СВ',  200, 5, 30, 600,    2400,   1, 10)


total_case = 15
all_blocks = [RG, IPSM, KVS, ZIV, FTS, KG_SV]
rangs = {
    'prop_1': [0.25, 1],
    'prop_2': [0.3,  1],
    'prop_3': [0.2, -1],
    'prop_4': [0.15, -1],
    'prop_5': [0.1, 1]
}

optimum = opt(rangs)
print(optimum)
blocks = transform_params(all_blocks)

full_choice_result = full_choice_smart(blocks, total_case, optimum, rangs)[1]
exp_points = [(10, 90), (10, 90), (0.1, 0.9), (0.1, 0.9)]
# размер поп    10  90
# поколения     10  90
# кросоовер     0.1 0.9
# мутация       0.1 0.9

exp_comb = list(product(*exp_points))

results3 = {}
for exp in exp_comb:
    GA = GeneticAlg(blocks, total_case, optimum, rangs, exp[0], exp[1], exp[2], exp[3])
    print(exp)
    results3[exp] = []

    for i in range(3):                  # 3 эксперемента для каждого
        results_for_10_starts = []
        for pusk in range(10):             # 10 запусков алгоритма
            result_for_10_starts = GA.start()
            results_for_10_starts.append(result_for_10_starts[0][1])
        ga_result = np.array(results_for_10_starts).mean() - full_choice_result
        results3[exp].append(ga_result)
    results3[exp].append(np.array(results3[exp]).mean())

print(results3)

total_case = 45


RG = Block('РГ',        200, 5, 30, 600,    2400,   1, 12)
IPSM = Block('ИПСМ',    210, 4, 30, 600,    2600,   1, 12)
KVS = Block('КВС',      190, 4, 40, 700,    2000,   1, 12)
ZIV = Block('ЗИВ',      200, 5, 30, 600,    2300,   1, 12)
FTS = Block('ФТС',      180, 5, 30, 600,    2500,   1, 12)
KG_SV = Block('КГ-СВ',  200, 5, 30, 600,    2400,   1, 12)
PPK = Block('ППК',      205, 4, 30, 600,    2400,   1, 12)
all_blocks = [RG, IPSM, KVS, ZIV, FTS, KG_SV, RG, IPSM, PPK]
optimum = opt(rangs)
blocks = transform_params(all_blocks)

full_choice_result = full_choice_smart(blocks, total_case, optimum, rangs)[1]

results8 ={}
for exp in exp_comb:
    GA = GeneticAlg(blocks, total_case, optimum, rangs, exp[0], exp[1], exp[2], exp[3])
    print(exp)
    results8[exp] = []

    for i in range(3):                  # 3 эксперемента для каждого
        results_for_10_starts = []
        for pusk in range(10):             # 10 запусков алгоритма
            result_for_10_starts = GA.start()
            results_for_10_starts.append(result_for_10_starts[0][1])
        ga_result = np.array(results_for_10_starts).mean() - full_choice_result
        results8[exp].append(ga_result)
    results8[exp].append(np.array(results8[exp]).mean())

print(results8)



with open('results.csv', 'w') as f:
    f.write('F1,F2,F3,F4,F5,Ex1,Ex2,Ex3,Avg\n')
    for key, val in results3.items():
        f.write('3,{},{},{},{},{},{},{},{}\n'.format(key[0], key[1], key[2], key[3], val[0], val[1], val[2], val[3]))
    for key, val in results8.items():
        f.write('8,{},{},{},{},{},{},{},{}\n'.format(key[0], key[1], key[2], key[3], val[0], val[1], val[2], val[3]))