from main_tools import GeneticAlg
from transfer_to_bits import Block, opt, transform_params, full_choice

KG_SV = Block('КГ-СВ',  50, 1,   1, 3)
KVS = Block('КВС',      50, 60,  1, 8)
RG = Block('РГ',        50, 1,   4, 8)
IPSM = Block('ИПСМ',    50, 60,  1, 10)

total_case = 21
all_blocks = [KG_SV, KVS, RG, IPSM]
rangs = {
    'cost': [0.4, 1],
    'wires': [0.6, 0],
    #  'power':        [0.1, 1],
    #  'russian_mc':   [0.1, -1],
    #  'time_to_build':[0.1, -1],
    #  'count_elem':   [0.5, -1]
}

optimum = opt(rangs)
blocks = transform_params(all_blocks)
GA = GeneticAlg(blocks, total_case, optimum, rangs, 50, 10, 0.7, 0.1)

result = GA.start()
print(result)
print(result[0][1])

print(full_choice(blocks, total_case, optimum, rangs))