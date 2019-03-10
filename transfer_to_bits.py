types_blocks = ['КГ-СВ', 'КВС', 'РГ', 'ИПСМ']


class Block:
    def __init__(self, name, cost, wires, power, russian_mc, time_to_build, count_elem, min_blocks, max_blocks):
        self.name = name
        self.cost = cost
        self.wires = wires
        self.power = power
        self.russian_mc = russian_mc
        self.time_to_build = time_to_build
        self.count_elem = count_elem
        self.min_blocks = min_blocks
        self.max_blocks = max_blocks


KG_SV = Block('КГ-СВ', 500, 3, 2, 100, 3, 220, 1, 2)
KVS = Block('КВС', 420, 6, 2, 90, 2, 150, 1, 8)
RG = Block('РГ', 400, 6, 1.5, 90, 1.5, 170, 1, 8)
IPSM = Block('ИПСМ', 300, 4, 1.2, 30, 2, 100, 1, 10)

all_blocks = [KG_SV, KVS, RG, IPSM]
num_blocks = [2, 5, 2, 3]

rangs = {
    'cost': [0.2, -1],
    'wires': [0.2, 1],
    'power': [0.1, 1],
    'russian_mc': [0.2, 1],
    'time_to_build': [0.1, -1],
    'count_elem': [0.2, 1]
}

opt = 1 - sum([val[0] for val in rangs.values() if val[1] == -1])
print(opt)


def transform_params(blocks):
    block_new_coef = blocks[:]
    properties = [x for x in list(KG_SV.__dict__.keys()) if x not in ['name', 'min_blocks', 'max_blocks']]
    for property in properties:
        sum_proper = sum([x.__getattribute__(property) for x in blocks])
        for block in block_new_coef:
            block.__setattr__(property, block.__getattribute__(property)/sum_proper)
    return block_new_coef


def func_opt(num_blocks: list = [], blocks: list = []):
    properties = [x for x in list(KG_SV.__dict__.keys()) if x not in ['name', 'min_blocks', 'max_blocks']]
    global_func = []
    for property in properties:
        global_func.append(sum([(x.__getattribute__(property)*rangs[property][1]*rangs[property][0]) * y for x, y in zip(blocks, num_blocks)]))
    return abs(sum(global_func))




transformed_blocks = transform_params(all_blocks)

print(func_opt(num_blocks=num_blocks, blocks=transformed_blocks))


full_choice = {}
for kg in range(1,20):
    for kvs in range(1,11):
        for rg in range(1,9):
            for ip in range(1,11):
                temp_list = [str(kg), str(kvs), str(rg), str(ip)]
                full_choice[' '.join(temp_list)] = func_opt([kg, kvs, rg, ip], transformed_blocks)

print(full_choice)


best = ('randaom_best', 1111)
for k, v in full_choice.items():
    if (opt - v)**2 < best[1]:
        best = (k, (opt - v)**2)
        print(best)
print(full_choice[best[0]])