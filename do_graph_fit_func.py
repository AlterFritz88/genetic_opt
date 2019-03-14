from transfer_to_bits import *

KVS = Block('КВС',  10, 1,   1, 8)
RG = Block('РГ',    1, 4,   1, 8)

all_blocks = [KVS, RG]

rangs = {
    'cost': [0.3, 1],
    'wires': [0.7, -1],
    #  'power':        [0.1, 1],
    #  'russian_mc':   [0.1, -1],
    #  'time_to_build':[0.1, -1],
    #  'count_elem':   [0.5, -1]
}

optimum = opt(rangs)

transformed_blocks = transform_params(all_blocks)


full_choice = {}
for kg in range(1, 4):
    for kvs in range(1, 11):

        if sum([kg, kvs]) > total_case:
            continue
        temp_list = [str(kg), str(kvs)]
        full_choice[' '.join(temp_list)] = func_opt([kg, kvs], transformed_blocks, optimum)

full_choice_sorted = sorted(full_choice.items(), key=lambda kv: kv[1])
print(full_choice_sorted)