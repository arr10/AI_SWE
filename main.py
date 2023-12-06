from init_population import get_initial_population
from gp import gp

if __name__ == "__main__":
    init_population = get_initial_population()
    gp(init_population)