#!/usr/bin/env python3

import sys
import math
import random
import numpy
import copy
import solver_final

from common import print_solution, read_input
from deap import base
from deap import creator
from deap import tools


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def evaluate(cell, N):
    pathlength = 0;
    for i in range(len(cell)):
        pathlength += distance(cell[i], cell[(i+1) % N])
    return pathlength

def evaluate(route, dist, N):
    pathlength = 0;
    for i in range(len(route)):
        pathlength += dist[route[i]][route[(i+1) % N]]
    return pathlength

def myshuffle(l):
    random.shuffle(l)
    return l

class Cell(object):
    def __init__(self, r, a, f):
        self.route = copy.deepcopy(r)
        self.age = a
        self.fitness = f

    def getRoute(self):
        return self.route

    def setRoute(self, r):
        self.route = copy.deepcopy(r)

    def getAge(self):
        return self.age

    def setAge(self, a):
        self.age = a

    def getFitness(self):
        return self.fitness

    def setFitness(self, f):
        self.fitness = f

    def addAge(self):
        self.age += 1

    def swap(self, i, j):
        self.route[i], self.route[j] = self.route[j], self.route[i]


def solve(cities):
    MAXAGE = 10
    MAXPOP = 100
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    solution = solver_final.solve(cities)

    pop = []
    hyppops = []
    for i in range(MAXPOP):
        pop.append(Cell(solution, 0, evaluate(solution, dist, N)))

    for generation in range(10000):

        clones = copy.deepcopy(pop)

        for clone in clones:
            for i in range(1):
                pos = random.randrange(5, N - 5)
                clone.swap(pos, random.randrange(pos - 5, pos + 5))

            newfit = evaluate(clone.getRoute(), dist, N)

            if newfit < clone.getFitness():
                hyppops.append(Cell(copy.deepcopy(clone.getRoute()), 0, newfit))
            else:
                hyppops.append(Cell(copy.deepcopy(clone.getRoute()), clone.getAge(), newfit))

        for p in pop:
            p.addAge()
            if (MAXAGE < p.getAge()) and (random.random() < 0.5):
                pop.remove(p)

        for hyppop in hyppops:
            hyppop.addAge()
            if (MAXAGE < hyppop.getAge()) and (random.random() < 0.5):
                hyppops.remove(hyppop)


        for hyppop in hyppops:
            pop.append(hyppop)

        while MAXPOP < len(pop):
            maxfit = pop[0].getFitness()
            maxpop = 0

            for i in range(len(pop)):
                if maxfit < pop[i].getFitness():
                    maxfit = pop[i].getFitness()
                    maxpop = i
            pop.pop(maxpop)

        while len(pop) < MAXPOP:
            newRoute = random.shuffle(solution)
            pop.append(Cell(newRoute), 0, evaluate(newRoute, dist, N))

        lowest = pop[0].getFitness()
        lowestpop = 0
        average = 0

        for i in range(len(pop)):
            average += pop[i].getFitness()
            if pop[i].getFitness() < lowest:
                lowest = pop[i].getFitness()
                lowestpop = i
        solution = pop[lowestpop].route
        pop[lowestpop].setAge(0)
        average = average/len(pop)
        print(generation)
        print(average)
        print(lowest)
        clones.clear()
        hyppops.clear()

        #for p in pop:
            #print(p.getRoute())

    return solution


if __name__ == '__main__':
    assert len(sys.argv) > 1
    solution = solve(read_input(sys.argv[1]))
    print_solution(solution)
