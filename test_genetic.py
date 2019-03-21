import numpy as np

from main_tools import GeneticAlg
from transfer_to_bits import Block, opt, transform_params, full_choice, full_choice_smart

KG_SV = Block('КГ-СВ',  50, 1,   1, 3)
KVS = Block('КВС',      50, 60,  1, 8)
RG = Block('РГ',        50, 1,   4, 8)
IPSM = Block('ИПСМ',    50, 60,  1, 8)

total_case = 21
all_blocks = [KG_SV, KVS, RG, IPSM]
rangs = {
    'cost': [0.4, 1],
    'wires': [0.6, -1],
    #  'power':        [0.1, 1],
    #  'russian_mc':   [0.1, -1],
    #  'time_to_build':[0.1, -1],
    #  'count_elem':   [0.5, -1]
}

optimum = opt(rangs)
blocks = transform_params(all_blocks)
GA = GeneticAlg(blocks, total_case, optimum, rangs, 100, 200, 0.7, 0.1)

results = []
'''
for i in range(10):
    result = GA.start()
    results.append(result[0][1])
ga_result = np.array(results).mean()
print(np.array(results).mean())
'''

full_choice_ans = full_choice(blocks, total_case, optimum, rangs)[0][1]
print(full_choice_ans)
full_choice_smart_ans = full_choice_smart(blocks, total_case, optimum, rangs)
print(full_choice_smart_ans)

