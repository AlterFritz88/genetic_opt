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


RG = Block('РГ',        200, 5, 30, 600,    2400,   1, 10)
IPSM = Block('ИПСМ',    210, 4, 30, 600,    2600,   1, 10)
KVS = Block('КВС',      190, 4, 40, 700,    2000,   1, 10)
ZIV = Block('ЗИВ',      200, 5, 30, 600,    2300,   1, 10)
FTS = Block('ФТС',      180, 5, 30, 600,    2500,   1, 10)
KG_SV = Block('КГ-СВ',  200, 5, 30, 600,    2400,   1, 10)
PPK = Block('ППК',      205, 4, 30, 600,    2400,   1, 10)

#первый эксеремент
total_case = 15
all_blocks = [RG, IPSM, KVS, ZIV, FTS, KG_SV]


optimum = opt(rangs)
blocks = transform_params(all_blocks)

full_choice_result = full_choice_smart(blocks, total_case, optimum, rangs)[1]

GA = GeneticAlg(blocks, total_case, optimum, rangs, 50, 50, 0.8, 0.05)

results_for_10_starts = []
for pusk in range(10):             # 10 запусков алгоритма
    result_for_10_starts = GA.start()
    results_for_10_starts.append(result_for_10_starts[0][1])
ga_result = np.array(results_for_10_starts).mean() - full_choice_result
exp_res_dict[3] = ga_result

#второй эксперемент
total_case = 17
all_blocks = [RG, IPSM, KVS, ZIV, FTS, KG_SV]


optimum = opt(rangs)
blocks = transform_params(all_blocks)

full_choice_result = full_choice_smart(blocks, total_case, optimum, rangs)[1]

GA = GeneticAlg(blocks, total_case, optimum, rangs, 50, 50, 0.8, 0.05)

results_for_10_starts = []
for pusk in range(10):             # 10 запусков алгоритма
    result_for_10_starts = GA.start()
    results_for_10_starts.append(result_for_10_starts[0][1])
ga_result = np.array(results_for_10_starts).mean() - full_choice_result
exp_res_dict[4] = ga_result

#третий

total_case = 22
all_blocks = [RG, IPSM, KVS, ZIV, FTS, KG_SV]


optimum = opt(rangs)
blocks = transform_params(all_blocks)

full_choice_result = full_choice_smart(blocks, total_case, optimum, rangs)[1]

GA = GeneticAlg(blocks, total_case, optimum, rangs, 50, 50, 0.8, 0.05)

results_for_10_starts = []
for pusk in range(10):             # 10 запусков алгоритма
    result_for_10_starts = GA.start()
    results_for_10_starts.append(result_for_10_starts[0][1])
ga_result = np.array(results_for_10_starts).mean() - full_choice_result
exp_res_dict[5] = ga_result

#четвертый
total_case = 25


RG = Block('РГ',        200, 5, 30, 600,    2400,   1, 11)
IPSM = Block('ИПСМ',    210, 4, 30, 600,    2600,   1, 11)
KVS = Block('КВС',      190, 4, 40, 700,    2000,   1, 11)
ZIV = Block('ЗИВ',      200, 5, 30, 600,    2300,   1, 11)
FTS = Block('ФТС',      180, 5, 30, 600,    2500,   1, 11)
KG_SV = Block('КГ-СВ',  200, 5, 30, 600,    2400,   1, 11)
PPK = Block('ППК',      205, 4, 30, 600,    2400,   1, 11)
all_blocks = [RG, IPSM, KVS, ZIV, FTS, KG_SV, RG]
optimum = opt(rangs)
blocks = transform_params(all_blocks)

full_choice_result = full_choice_smart(blocks, total_case, optimum, rangs)[1]

GA = GeneticAlg(blocks, total_case, optimum, rangs, 50, 50, 0.8, 0.05)

results_for_10_starts = []
for pusk in range(10):             # 10 запусков алгоритма
    result_for_10_starts = GA.start()
    results_for_10_starts.append(result_for_10_starts[0][1])
ga_result = np.array(results_for_10_starts).mean() - full_choice_result
exp_res_dict[6] = ga_result


#пятый
total_case = 45
all_blocks = [RG, IPSM, KVS, ZIV, FTS, KG_SV, RG]


optimum = opt(rangs)
blocks = transform_params(all_blocks)

full_choice_result = full_choice_smart(blocks, total_case, optimum, rangs)[1]

GA = GeneticAlg(blocks, total_case, optimum, rangs, 50, 50, 0.8, 0.05)

results_for_10_starts = []
for pusk in range(10):             # 10 запусков алгоритма
    result_for_10_starts = GA.start()
    results_for_10_starts.append(result_for_10_starts[0][1])
ga_result = np.array(results_for_10_starts).mean() - full_choice_result
exp_res_dict[7] = ga_result



#шестой
total_case = 45


RG = Block('РГ',        200, 5, 30, 600,    2400,   1, 12)
IPSM = Block('ИПСМ',    210, 4, 30, 600,    2600,   1, 12)
KVS = Block('КВС',      190, 4, 40, 700,    2000,   1, 12)
ZIV = Block('ЗИВ',      200, 5, 30, 600,    2300,   1, 12)
FTS = Block('ФТС',      180, 5, 30, 600,    2500,   1, 12)
KG_SV = Block('КГ-СВ',  200, 5, 30, 600,    2400,   1, 12)
PPK = Block('ППК',      205, 4, 30, 600,    2400,   1, 12)
all_blocks = [RG, IPSM, KVS, ZIV, FTS, KG_SV, RG]
optimum = opt(rangs)
blocks = transform_params(all_blocks)

full_choice_result = full_choice_smart(blocks, total_case, optimum, rangs)[1]

GA = GeneticAlg(blocks, total_case, optimum, rangs, 50, 50, 0.8, 0.05)

results_for_10_starts = []
for pusk in range(10):             # 10 запусков алгоритма
    result_for_10_starts = GA.start()
    results_for_10_starts.append(result_for_10_starts[0][1])
ga_result = np.array(results_for_10_starts).mean() - full_choice_result
exp_res_dict[8] = ga_result


print(exp_res_dict)