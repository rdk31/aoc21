#!/usr/bin/env python

def get_count(fish, days):
    population = [0] * 9
    for f in fish:
        population[f] += 1

    for _ in range(days):
        p = population.pop(0)
        population[6] += p
        population.append(p)

    return sum(population)

with open("input.txt") as f:
    text = f.read()
text = text.splitlines()

fish = list(map(int, text[0].split(",")))

print(f"part1: {get_count(fish, 80)}")
print(f"part2: {get_count(fish, 256)}")
