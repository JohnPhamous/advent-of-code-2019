#!/usr/bin/python3
import math


def getFuel(mass):
    DIVISION_CONSTANT = 3.0
    return math.floor(float(mass) / DIVISION_CONSTANT) - 2


with open('./input') as file:
    line = file.readline()
    sum = 0
    while line:
        current_mass = int(line)
        sum += getFuel(current_mass)
        line = file.readline()
    print(sum)
