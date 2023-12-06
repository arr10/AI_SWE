import json
import os
from fitness import fitness
from crossover import crossover
from mutation import mutate
from selection import select


class Promt:
    def __init__(self, prompt):
        self.prompt = prompt
        self.fitness = 0

    def evaluate(self):
        self.fitness = fitness(self)


def gp(init_population):

    population = init_population

    pop_size = len(init_population)
    budget = 100
    count = 0

    rate_crossover = 1  # probability of crossover happening

    rate_mutation = 1  # probability of mutation happening

    select_const = 10  # number of prompts to be selected for random selection

    while count < budget:
        next_gen = []

        while len(next_gen) < len(population):

            p1 = select(select_const, population)
            p2 = select(select_const, population)

            o1, o2 = crossover(p1.prompt, p2.prompt, rate_crossover)

            o1 = mutate(o1, rate_mutation)
            o2 = mutate(o2, rate_mutation)

            o1, o2 = Promt(o1), Promt(o2)

            o1.evaluate()
            o2.evaluate()

            next_gen.append(o1)
            next_gen.append(o2)

        population.extend(next_gen)
        population = sorted(population, key=lambda x: x.fitness)
        population = population[:pop_size]

        best_solution = population[0]
        count += 1
        print(count, best_solution, best_solution.fitness)
        data = {}
        for i in range(len(population)):
            data[i] = {
                'prompt': population[i].prompt,
                'fitness': population[i].fitness
            }
        with open(f'./results/generation_{count}_prompts.json', 'w') as f:
            json.dump(data, f, indent=4)

    return best_solution