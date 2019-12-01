#!/usr/bin/python3
import math


def get_fuel(mass):
    DIVISION_CONSTANT = 3.0
    return math.floor(float(mass) / DIVISION_CONSTANT) - 2


with open('./input') as file:
    line = file.readline()
    total_fuel = 0

    while line:
        current_mass = int(line)
        new_fuel = get_fuel(current_mass)

        fuel_for_fuel = get_fuel(new_fuel)

        while fuel_for_fuel > 0:
            new_fuel += fuel_for_fuel
            fuel_for_fuel = get_fuel(fuel_for_fuel)

        total_fuel += new_fuel
        line = file.readline()
    print(int(total_fuel))
