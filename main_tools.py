import random
from transfer_to_bits import Block, func_opt, transform_params

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
    pairs = []
    for i in range(num_pairs):
        par_1 = random.choice(temp_population)
        temp_population.remove(par_1)
        par_2 = random.choice(temp_population)
        temp_population.remove(par_2)
        print(par_1[1], par_2[1])
        if par_1[1] < par_2[1]:
            new_generation.append(par_1)
        else:
            new_generation.append(par_2)
    return new_generation





if __name__ == '__main__':
    KG_SV = Block('КГ-СВ', 50, 1, 1, 3)
    KVS = Block('КВС', 50, 60, 1, 8)
    RG = Block('РГ', 50, 1, 1, 8)
    IPSM = Block('ИПСМ', 50, 60, 1, 10)
    total_case = 20
    all_blocks = [KG_SV, KVS, RG, IPSM]
    rangs = {
        'cost': [0.4, 0],
        'wires': [0.6, 1],
        #  'power':        [0.1, 1],
        #  'russian_mc':   [0.1, -1],
        #  'time_to_build':[0.1, -1],
        #  'count_elem':   [0.5, -1]
    }
    opt = sum([val[0] * val[1] for val in rangs.values()])
    transformed_blocks = transform_params(all_blocks)


    init_pop = creat_init_population(100, transformed_blocks, total_case)
    first_gen = get_fit_functions(init_pop, transformed_blocks, opt)
    print(tournament_selection(first_gen))
