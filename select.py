import random

def select(k, population):
    selected = random.sample(population, k)
    return sorted(selected, key=lambda x:x.fitness)[0]
