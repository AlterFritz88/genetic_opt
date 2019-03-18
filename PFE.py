from main_tools import GeneticAlg
from transfer_to_bits import opt, transform_params, full_choice

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
GA = GeneticAlg(blocks, total_case, optimum, rangs, 100, 5, 0.7, 0.1)
print(GA.start())

print(full_choice(blocks, total_case, optimum, rangs))
