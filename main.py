import random
import math
import numpy as np


def print_2d_list(list):
    s = [[str(e) for e in row] for row in list]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))


def generate_chromosome(chromosome_size):
    chromosome = []
    for i in range(chromosome_size):
        chromosome.append(random.randint(0, 1))
    return chromosome


def generate_population(population_size, chromosome_size):
    population = []
    for i in range(population_size):
        population.append(generate_chromosome(chromosome_size))

    return population


def calculate_population_fitness(population):
    fitness_values = []
    for chromosome in population:
        fitness_values.append(fitness(chromosome))
    return fitness_values


def roulette_select(population, fitness_values):
    sum_fitness = sum(fitness_values)

    selection_id = -1
    random_num = random.uniform(0, sum_fitness)
    for i, fitness in enumerate(fitness_values):
        if random_num <= 0:
            selection_id = i
            break
        random_num -= fitness
    return population[selection_id]


def sample_population(population, fitness_values, selection_rate=0.5):
    # separate the population in mating population and rest
	
    population_size = len(population)
    num_of_selected_chromosomes = int(selection_rate * population_size)
    mating_population = []
    for i in range(num_of_selected_chromosomes):
        parent = roulette_select(population, fitness_values)
        mating_population.append(parent)
        """
        # remove from initial population, so it will not be selected twice
        population.remove(parent)
        fitness_values.remove(fitness)
        """

    return mating_population


def crossover(mating_pool):
    for i in range(0, len(mating_pool)-1, 2):
        parent1 = mating_pool[i]
        parent2 = mating_pool[i+1]

        # Perform single-point crossover
        # pick random number starting from 1 because if we start from 0 (change all bits) it will make no difference
        crossover_bit = random.randint(1, len(parent1) - 1)
        parent1[crossover_bit:], parent2[crossover_bit:] = parent2[crossover_bit:], parent1[crossover_bit:]  # swap bits

        mating_pool[i] = parent1
        mating_pool[i+1] = parent2

    return mating_pool


def preserve_top(population, fitness_values, preserve_rate):
    population_size = len(population)

    # sort population by fitness descending
    idx = np.argsort(fitness_values)[::-1]
    population = np.array(population)[idx]

    num_of_preserved_chromosomes = math.ceil(preserve_rate * population_size)
    return population[:num_of_preserved_chromosomes]


def mutate(population, mutation_probability):
    for i in range(len(population)):
        random_number = random.random()
        if random_number < mutation_probability:
            # current chromosome was selected for mutation
            current_chromosome = population[i]
            random_number = random.randint(0, len(current_chromosome) - 1)
            current_chromosome[random_number] = 1 - current_chromosome[random_number]  # make 0->1 and 1->0
            population[i] = current_chromosome

    return population


def create_generation(population, fitness_values, mating_probability, mutation_probability):
    # Crossover
    mating_pool = sample_population(population, fitness_values, mating_probability)
    parents = crossover(mating_pool)

    # Preservation
    preserved_population = preserve_top(population, fitness_values, 1 - mating_probability)

    # New generation
    new_population = parents
    new_population.extend(preserved_population)

    # Mutations
    new_population = mutate(new_population, mutation_probability)

    return new_population


def fitness(chromosome):
	# current problem: find the chromosome with all bits 1
    return sum(chromosome) # how many bits are 1
    # different problem: find the chromosome with all bits 0
	# return len(chromosome) - sum(chromosome) # how many bits are 0


def run_genetic_algorithm(population_size, chromosome_size, mating_probability, mutation_probability, max_fitness):
    # Create initial population
    population = generate_population(population_size, chromosome_size)
    fitness_values = calculate_population_fitness(population)

    # Run genetic algorithm
    generations_count = 0
    while max(fitness_values) < max_fitness:
        generations_count += 1
        population = create_generation(population, fitness_values, mating_probability, mutation_probability)
        fitness_values = calculate_population_fitness(population)

        #print(str(generations_count) + ")", "Max:", max(fitness_values))

    max_idx = np.argmax(fitness_values)
    best_chromosome = population[max_idx]

    return generations_count, best_chromosome


def main():

    # Define problem parameters
    population_size = 100           # n
    chromosome_size = 20	        # l
    max_fitness = chromosome_size

    mating_probability = 0.7        # Pδ
    mutation_probability = 0.001    # Pμ

    iterations = 5	# Repeat experiment to count average number of generations needed to reach best solution

    generations_sum = 0
    for i in range(iterations):
        print("Iteration:", i+1)
        generations, best_chromosome = run_genetic_algorithm(population_size, chromosome_size, mating_probability,
                                                             mutation_probability, max_fitness)
        generations_sum += generations
        print("\t", generations, "generations needed")
        print("\t", "Solution:", best_chromosome)

    print("Average number of generations:", generations_sum/iterations)


if __name__ == "__main__":
    main()


