import random
from itertools import product

import numpy as np

class Block:
    def __init__(self, name, cost, wires, min_blocks, max_blocks):
        self.name = name
        self.cost = cost
        self.wires = wires
        self.min_blocks = min_blocks
        self.max_blocks = max_blocks
        '''
        self.power = power
        self.russian_mc = russian_mc
        self.time_to_build = time_to_build
        self.count_elem = count_elem
        self.min_blocks = min_blocks
        self.max_blocks = max_blocks
        '''

def transform_params(blocks):
    block_new_coef = blocks[:]
    properties = [x for x in list(blocks[0].__dict__.keys()) if x not in ['name', 'min_blocks', 'max_blocks']]
    for property in properties:
        sum_proper = sum([x.__getattribute__(property) for x in blocks])
        for block in block_new_coef:
            block.__setattr__(property, block.__getattribute__(property) / sum_proper)
    return block_new_coef


def func_opt(rangs, num_blocks: list = [], blocks: list = [], opt=1):
    properties = [x for x in list(blocks[0].__dict__.keys()) if x not in ['name', 'min_blocks', 'max_blocks']]
    global_func = []
    range_blocks = [x.max_blocks + 1 - x.min_blocks for x in blocks]
    otn_num_blocks = [x / total_case for x, total_case in zip(num_blocks, range_blocks)]
    otn_num_blocks_minus = [1 - (x / total_case) for x, total_case in zip(num_blocks, range_blocks)]

    for property in properties:
        if rangs[property][1] == 1:
            global_func.append(sum(
                [(x.__getattribute__(property) * rangs[property][1] * rangs[property][0]) * y for x, y in
                 zip(blocks, otn_num_blocks)]))
        else:
            global_func.append(sum(
                [(x.__getattribute__(property) * rangs[property][1] * rangs[property][0]) * y for x, y in
                 zip(blocks, otn_num_blocks_minus)]))

    return (opt - sum(global_func))**2


def opt(rangs):
    return sum([val[0] * val[1] for val in rangs.values()])


def full_choice(blocks, total_case, opt, rangs):

    range_blocks = [range(x.min_blocks, x.max_blocks+1) for x in blocks]
    output_comb = list(product(*range_blocks))
    output_comb = [list(x) for x in output_comb if sum(x) <= total_case]

    temp_list = [' '.join(str(y) for y in x) for x in output_comb]

    full_choice = {x: func_opt(rangs, y, blocks, opt) for x, y in zip(temp_list, output_comb)}
    full_choice_sorted = sorted(full_choice.items(), key=lambda kv: kv[1])
    return full_choice_sorted

def full_choice_smart(blocks, total_case, opt, rangs):
    range_blocks = [range(x.min_blocks, x.max_blocks + 1) for x in blocks]
    output_comb = product(*range_blocks)
    print('finding by full choice....')
    min_num = ('xxx',100)
    counter_comb = 0
    try:
        while 1:
            combination = list(output_comb.__next__())
            if sum(combination) <= total_case:
                result = func_opt(rangs, combination, blocks, opt)
                counter_comb += 1
                if result < min_num[1]:
                    min_num = (' '.join([str(x) for x in combination]), result)
    except StopIteration:
        print('Total number of combinations: {}'.format(counter_comb))
        return min_num

def find_number_combinations(total_case, n_types, minimum, maximum):
    range_blocks = [range(minimum, maximum + 1) for x in range(n_types)]
    output_comb = product(*range_blocks)
    counter_comb = 0

    try:
        while 1:
            combination = [*output_comb.__next__()]
            #print(combination)
            if sum(combination) <= total_case:
                counter_comb += 1
    except StopIteration:
        print('Total number of combinations: {}'.format(counter_comb))

if __name__ == '__main__':
    find_number_combinations(45, 9, 1, 14)