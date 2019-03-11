import random
from transfer_to_bits import Block

def creat_init_population(number_creatures, blocks, box_size):
    creatures = []
    constraints = [(x.min_blocks, x.max_blocks) for x in blocks]
    while len(creatures) <= number_creatures:
        creature = [random.randint(constraint[0], constraint[1]) for constraint in constraints]
        if sum(creature) <= box_size:
            creatures.append(creature)
    return creatures

if __name__ == '__main__':
    KG_SV = Block('КГ-СВ', 50, 1, 1, 3)
    KVS = Block('КВС', 50, 60, 1, 8)
    RG = Block('РГ', 50, 1, 1, 8)
    IPSM = Block('ИПСМ', 50, 60, 1, 10)
    total_case = 20
    all_blocks = [KG_SV, KVS, RG, IPSM]

    print(creat_init_population(100, all_blocks, total_case))
