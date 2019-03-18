import random
from itertools import product

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
    print(full_choice_sorted)


if __name__ == '__main__':

    transformed_blocks = transform_params(all_blocks)

    num_blocks = [1, 5, 1, 1]
    print(func_opt(num_blocks=num_blocks, blocks=transformed_blocks, opt=optimum))

    full_choice = {}
    for kg in range(1, 4):
        for kvs in range(1, 11):
            for rg in range(1, 9):
                for ip in range(1, 11):
                    if sum([kg, kvs, rg, ip]) > total_case:
                        continue
                    temp_list = [str(kg), str(kvs), str(rg), str(ip)]
                    full_choice[' '.join(temp_list)] = func_opt([kg, kvs, rg, ip], transformed_blocks, optimum)

    full_choice_sorted = sorted(full_choice.items(), key=lambda kv: kv[1])
    print(full_choice_sorted)

    # random test
    random_ch = {}
    for i in range(90000):
        num_blocks = [random.randint(1, 10) for x in range(4)]
        if sum(num_blocks) > total_case:
            continue
        temp_list = [str(x) for x in num_blocks]
        random_ch[' '.join(temp_list)] = func_opt(num_blocks, transformed_blocks, optimum)

    random_ch_sorted = sorted(random_ch.items(), key=lambda kv: kv[1])
    print(random_ch_sorted)