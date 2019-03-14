import random
import math
from transfer_to_bits import Block, func_opt, transform_params


def hex2bin(str, lenght):
    """
    Переводчик hex, oct str в bin str
    """
    a = int(str)
    return format(a, '0>{}b'.format(lenght))

def creat_init_population(number_creatures, blocks, box_size):
    creatures = []
    constraints = [(x.min_blocks, x.max_blocks) for x in blocks]
    while len(creatures) != number_creatures:
        creature = [random.randint(constraint[0], constraint[1]) for constraint in constraints]
        if sum(creature) <= box_size and creature not in creatures:
            creatures.append(creature)
    return creatures


def get_fit_functions(population, blocks, opt):
    values = {' '.join(str(x) for x in person): func_opt(person, blocks, opt) for person in population}
    sorted_values = sorted(values.items(), key=lambda kv: kv[1])
    return sorted_values


def tournament_selection(population):
    num_pairs = len(population) // 2
    temp_population = population[:]
    new_generation = []
    for i in range(num_pairs):
        par_1 = random.choice(temp_population)
        temp_population.remove(par_1)
        par_2 = random.choice(temp_population)
        temp_population.remove(par_2)
        if par_1[1] < par_2[1]:
            new_generation.append(par_1)
        else:
            new_generation.append(par_2)
    return new_generation



def crossover_random_point(generation, blocks, crossover_chance=0.7):
    num_pairs = len(generation) // 2
    creatures = [code_chromosome(x[0], blocks) for x in generation]
    print(creatures)
    new_generation = []
    for i in range(num_pairs):
        par_1 = random.choice(creatures)
        creatures.remove(par_1)
        par_2 = random.choice(creatures)
        creatures.remove(par_2)
        if random.random() < crossover_chance:
            cross_point = random.randint(1, len(par_1) - 2)
            child_1 = par_1[:cross_point] + par_2[cross_point:]
            child_2 = par_2[:cross_point] + par_1[cross_point:]
            new_generation.append(child_1)
            new_generation.append(child_2)
        else:
            new_generation.append(par_1)
            new_generation.append(par_2)
    print(len(new_generation))



def code_chromosome(creature, blocks):
    get_max_len = [math.ceil(math.log2(x.max_blocks + 1 - x.min_blocks)) for x in blocks]
    creature_splited = creature.split(' ')

    creature_transformed = [int(x) - y.min_blocks for x, y in zip(creature_splited, blocks)]
    coded = [hex2bin(x, y) for x, y in zip(creature_transformed, get_max_len)]
    return ''.join(coded)


def get_chromosome_params(blocks):
    get_max_len = [math.ceil(math.log2(x.max_blocks - x.min_blocks)) for x in blocks]
    lenght_chromosome = sum(get_max_len)
    return get_max_len, lenght_chromosome



if __name__ == '__main__':

    KG_SV = Block('КГ-СВ', 50, 1,   1, 3)
    KVS = Block('КВС', 50, 60,      1, 8)
    RG = Block('РГ', 50, 1,         5, 8)
    IPSM = Block('ИПСМ', 50, 60,    1, 10)

    total_case = 20
    all_blocks = [KG_SV, KVS, RG, IPSM]
    rangs = {
        'cost': [0.4, 1],
        'wires': [0.6, 0],
        #  'power':        [0.1, 1],
        #  'russian_mc':   [0.1, -1],
        #  'time_to_build':[0.1, -1],
        #  'count_elem':   [0.5, -1]
    }
    opt = sum([val[0] * val[1] for val in rangs.values()])
    print('opt', opt)
    transformed_blocks = transform_params(all_blocks)

    init_pop = creat_init_population(100, transformed_blocks, total_case)
    first_gen = get_fit_functions(init_pop, transformed_blocks, opt)
    selected = tournament_selection(first_gen)
    print(crossover_random_point(selected, all_blocks))

    print(code_chromosome('3 5 5 6', all_blocks))
