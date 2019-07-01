# Genetic-Algorithm-from-scratch
A genetic algorithm implementation in python where chromosomes are sequences of bits.
As a sample problem I used the problem of creating a chromosome with all bits equal to 1.
This can be changed by editing the ``fitness`` function (see example in comments) in the file [main.py](/main.py#L125).

## Parameters
    population_size = 100
    chromosome_size = 20
    max_fitness = chromosome_size

    mating_probability = 0.7
    mutation_probability = 0.001

    iterations = 5

- **Population size**: how many chromosomes to be generated
- **Chromosome size**: how many bits on every chromosome
- **Max fitness**: The fitness we want to achieve
- **Mating probability**: What percentage of population to use as mating pool
- **Mutation probability**: How probable it is that one chromosome will mutate
- **Iterations**: How many times to run the experiment (for counting the average generations needed)

## Process Explained

**Step 1** <br />
Generate initial population with random bits

**Step 2** <br />
Choose some chromosomes (according to ``mating_probability``) for mating (mating pool) using [roulette wheel selection](https://en.wikipedia.org/wiki/Fitness_proportionate_selection)

**Step 3** <br />
Perform [single-point crossover](https://en.wikipedia.org/wiki/Crossover_(genetic_algorithm)#Single-point_crossover) on chromosomes of mating pool

**Step 4** <br />
Preserve top chromosomes of current generation (as many as needed in order to keep the same population size)

**Step 5** <br />
Perform [mutation](https://en.wikipedia.org/wiki/Mutation_(genetic_algorithm)) on some chromosomes of the new population (according to ``mutation_probability``) by changing one random bit

**Step 6** <br />
Count the fitness of new chromosomes. If ``max_fitness`` has not been reached then go to Step 2.

## Execution

The source code has been tested and runs using Python 3. You can run it using:

    python3 main.py
    
Example result:

    Iteration 1
        Generations needed: 34
        Solution: [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]
    Iteration 2
        Generations needed: 30
        Solution: [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]
    Iteration 3
        Generations needed: 158
        Solution: [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]
    Iteration 4
        Generations needed: 20
        Solution: [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]
    Iteration 5
        Generations needed: 24
        Solution: [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]
    Average number of generations: 53.2


