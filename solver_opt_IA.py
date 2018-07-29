#!/usr/bin/env python3

import sys
import math
import random
import numpy

from common import print_solution, read_input
from deap import base
from deap import creator
from deap import tools


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def evaluate(cell):
    pathlength = 0;
    for i in range(len(cell)):
        pathlength += distance(cell[i], cell[i+1])
    return pathlength

def myshuffle(l):
    random.shuffle(l)
    return l

def solve(cities):
    MAXAGE = 5
    MAXPOP = 100
    N = len(cities)
    toolbox = base.Toolbox()

    creator.create("FitnessMin", base.Fitness, weights = (-1.0,))
    creator.create("Cell", list, fitness = creator.FitnessMin, age = None)

    toolbox.register("evalate", evaluate)
    toolbox.register("mutate", tools.mutShuffleIndexes, indpb = 0.2)

    toolbox.register("shuffle", random.shuffle, cities)

    toolbox.register("attribute", toolbox.shuffle, 10)
    toolbox.register("cell", tools.initIterate, creator.Cell, toolbox.attribute)
    toolbox.register("poplation", tools.initRepeat, list, toolbox.cell)

    pop = toolbox.poplation(n=10)

    fitnesses = list(map(toolbox.evalate, pop))
    for indiv, fit in zip(pop, fitnesses):
        indiv.fitness.values = fit
        indiv.age = 0

    for generation in range(10):

        clones = list(map(toolbox.clone, pop))
        hyppops = list(map(toolbox.mutate, clone))

        for clone, hyppop in zip(clones, hyppops):
            mutation = toolbox.mutate(clone.list)
            newfit = toolbox.evalate(mutation)
            if newfit < clone.fitness:
                hyppop.list = mutation
                hyppop.age = 0
            else:
                hyppop.list = mutation

        for p in pop:
            p.age += 1
            if MAXAGE < p.age:
                pop.remove(p)

        for hyppop in hyppops:
            hyppop.age += 1
            if MAXAGE < hyppop.age:
                hyppops.remove(hyppop)


        for hyppop in hyppops:
            pop.append(hyppop)

        while MAXPOP < len(pop):
            maxfit = pop[0].fitness.values
            maxpop = 0

            for i in pop.length():
                if maxfit < pop[i].fitness.values:
                    maxfit = pop[i].fitness.values
                    maxpop = i
            pop.pop(maxpop)

        while pop.length() < MAXPOP:
            pop.append(toolbox.cell())

        lowest = pop[0].fitness.values
        lowestpop = 0

        for i in pop.length():
            if pop[i].fitness.values < lowest:
                lowest = pop[i].fitness.values
                lowestpop = i
        solution = pop[lowestpop].list

    return solution


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
