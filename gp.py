import json
import os
from fitness import fitness
from crossover import crossover
from mutation import mutate
from selection import select
import random
from testcase_fitness import testcase_fitness
from codecorrection_fitness import bugfix_fitness


class Promt:
    def __init__(self, prompt, data_type):
        self.prompt = prompt
        self.fitness = -1
        self.data_type = data_type

    def evaluate(self):
        if self.fitness == -1:
            if self.data_type == "reasoning":
                self.fitness = fitness(self.prompt)
            elif self.data_type == "testcase":
                self.fitness = testcase_fitness(self.prompt)
            elif self.data_type == "bugfix":
                self.fitness = bugfix_fitness(self.prompt)


def gp(init_population, data_type):

    population = init_population
    population = random.sample(population, 10)
    for i in range(len(population)):
        population[i] = Promt(population[i], data_type)
        population[i].evaluate()

    pop_size = len(init_population)
    budget = 10
    count = 0

    rate_crossover = 1  # probability of crossover happening

    rate_mutation = 1  # probability of mutation happening

    select_const = 3  # number of prompts to be selected for random selection

    while count < budget:
        next_gen = []

        while len(next_gen) < len(population):

            p1 = select(select_const, population)
            p2 = select(select_const, population)
            try:
                o1, o2 = crossover(p1.prompt, p2.prompt, rate_crossover)
            except:
                x = 1
            try:
                o1 = mutate(o1, rate_mutation)
                o2 = mutate(o2, rate_mutation)
            except:
                x = 1

            o1, o2 = Promt(o1, data_type), Promt(o2, data_type)

            o1.evaluate()
            o2.evaluate()

            next_gen.append(o1)
            next_gen.append(o2)

        population.extend(next_gen)
        population = sorted(population, key=lambda x: x.fitness, reverse=True)
        population = population[:pop_size]

        best_solution = population[0]
        count += 1
        print(count, best_solution.prompt, best_solution.fitness)
        data = {}
        for i in range(len(population)):
            data[i] = {
                'prompt': population[i].prompt,
                'fitness': population[i].fitness
            }
        with open(f'./results/generation_{count}_prompts.json', 'w') as f:
            json.dump(data, f, indent=4)

    return best_solution