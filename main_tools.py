import random
import math
from itertools import accumulate, chain
from transfer_to_bits import Block, func_opt, transform_params


class GeneticAlg:

    def __init__(self, blocks, box_size, opt, rangs, n_population, generations, cross_chance, mutate_chance):
        self.n_population = n_population
        self.rangs = rangs
        self.box_size = box_size
        self.opt = opt
        self.blocks = blocks
        self.cross_chance = cross_chance
        self.mutate_chance = mutate_chance
        self.generations = generations

    def hex2bin(self, str, lenght):
        """
        Переводчик hex, oct str в bin str
        """
        a = int(str)
        return format(a, '0>{}b'.format(lenght))

    def creat_init_population(self, n_pop):
        creatures = []
        constraints = [(x.min_blocks, x.max_blocks) for x in self.blocks]
        while len(creatures) != n_pop:
            creature = [random.randint(constraint[0], constraint[1]) for constraint in constraints]
            if sum(creature) <= self.box_size and creature not in creatures:
                creatures.append(creature)
        return creatures


    def get_fit_functions(self, population):
        values = {' '.join(str(x) for x in person): func_opt(self.rangs, person, self.blocks, self.opt) for person in population}
        sorted_values = sorted(values.items(), key=lambda kv: kv[1])
        return sorted_values


    def tournament_selection(self, population):
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



    def crossover_random_point(self, generation):
        num_pairs = len(generation) // 2
        creatures = [self.code_chromosome(x[0]) for x in generation]
        new_generation = []
        for i in range(num_pairs):
            par_1 = random.choice(creatures)
            creatures.remove(par_1)
            par_2 = random.choice(creatures)
            creatures.remove(par_2)
            if random.random() < self.cross_chance:
                cross_point = random.randint(1, len(par_1) - 2)
                child_1 = par_1[:cross_point] + par_2[cross_point:]
                child_2 = par_2[:cross_point] + par_1[cross_point:]
                new_generation.append(child_1)
                new_generation.append(child_2)
                new_generation.append(par_1)
                new_generation.append(par_2)
            else:
                new_generation.append(par_1)
                new_generation.append(par_2)
                new_generation.append(par_1)
                new_generation.append(par_2)
        return new_generation

    def crossover_by_block(self, generation):
        num_pairs = len(generation) // 2
        creatures = [self.code_chromosome(x[0]) for x in generation]
        new_generation = []
        lens, _ = self.get_chromosome_params()
        lens = list(accumulate(lens))[:-1]
        for i in range(num_pairs):
            par_1 = random.choice(creatures)
            creatures.remove(par_1)
            par_2 = random.choice(creatures)
            creatures.remove(par_2)
            if random.random() < self.cross_chance:
                cross_point = random.choice(lens)
                child_1 = par_1[:cross_point] + par_2[cross_point:]
                child_2 = par_2[:cross_point] + par_1[cross_point:]
                new_generation.append(child_1)
                new_generation.append(child_2)
            else:
                new_generation.append(par_1)
                new_generation.append(par_2)
                new_generation.append(par_1)
                new_generation.append(par_2)
        return new_generation


    def mutation(self, generation):
        mutated_generation = []
        for creature in generation:
            mutated_creature = []
            for bit in creature:
                if random.random() < self.mutate_chance:
                    if bit == '1':
                        mutated_creature.append('0')
                    else:
                        mutated_creature.append('1')
                else:
                    mutated_creature.append(bit)
            mutated_generation.append(''.join(mutated_creature))
        return mutated_generation


    def code_chromosome(self, creature):
        get_max_len = [math.ceil(math.log2(x.max_blocks + 1 - x.min_blocks)) for x in self.blocks]
        creature_splited = creature.split(' ')

        creature_transformed = [int(x) - y.min_blocks for x, y in zip(creature_splited, self.blocks)]
        coded = [self.hex2bin(x, y) for x, y in zip(creature_transformed, get_max_len)]
        return ''.join(coded)

    def decode_chromosome(self, creature):
        max_len, len_chromosome = self.get_chromosome_params()
        decoded_chromosome = []
        for i in max_len:
            decoded_chromosome.append(creature[:i])
            creature = creature[i:]
        decoded_chromosome = [int(x, 2) for x in decoded_chromosome]
        return decoded_chromosome


    def check_and_kill_chromosome(self, population):
        decoded_population = [self.decode_chromosome(x) for x in population]
        range_blocks = [range(x.min_blocks, x.max_blocks+1) for x in self.blocks]
        spartans_generation = [x for x in decoded_population if sum(x) <= self.box_size]
        new_spartans = []
        for spartan in spartans_generation:
            new_spartan = [x for x, y in zip(spartan, range_blocks) if x in y]
            if len(new_spartan) == len(range_blocks):
                new_spartans.append(new_spartan)
        if len(new_spartans) < self.n_population:
            add_creat = self.creat_init_population((self.n_population - len(new_spartans)))
            new_spartans = list(chain(new_spartans, add_creat))
        return new_spartans


    def get_chromosome_params(self):
        get_max_len = [math.ceil(math.log2(x.max_blocks + 1 - x.min_blocks)) for x in self.blocks]
        lenght_chromosome = sum(get_max_len)
        return get_max_len, lenght_chromosome

    def start(self):
        population = self.creat_init_population(self.n_population)
        for generation in range(self.generations):
            print('this is {} generation'.format(generation))
            population = self.get_fit_functions(population)
            population_selected = self.tournament_selection(population)
            population_crossovered = self.crossover_by_block(population_selected)
            population_mutated = self.mutation(population_crossovered)
            population_reducted = self.check_and_kill_chromosome(population_mutated)
            population = population_reducted[:]
        return self.get_fit_functions(population)


if __name__ == '__main__':

    KG_SV = Block('КГ-СВ', 50, 1,   1, 3)
    KVS = Block('КВС', 50, 60,      1, 8)
    RG = Block('РГ', 50, 1,         4, 8)
    IPSM = Block('ИПСМ', 50, 60,    1, 10)

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
    opt = sum([val[0] * val[1] for val in rangs.values()])
    print('opt', opt)
    transformed_blocks = transform_params(all_blocks)

    init_pop = creat_init_population(100, transformed_blocks, total_case)
    first_gen = get_fit_functions(init_pop, transformed_blocks, opt)
    print(first_gen)
    selected = tournament_selection(first_gen)
    after_cross = crossover_by_block(selected, all_blocks)
    mutated = mutation(after_cross, 0.05)

    spartans = check_and_kill_chromosome(mutated, total_case, all_blocks, 100)
    print(get_fit_functions(spartans, transformed_blocks, opt))


