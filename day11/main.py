#!/usr/bin/env python

import itertools
import copy

dirs = list(itertools.product([-1, 0, 1], [-1, 0, 1]))
dirs.remove((0, 0))

def check_energy_level(x, y, m):
    if type(m[y][x]) is int:
        m[y][x] += 1

        if m[y][x] > 9:
            m[y][x] = True
            for (dx, dy) in dirs:
                new_x = x - dx
                new_y = y - dy
                if new_y >= 0 and new_y < len(m) and new_x >= 0 and new_x < len(m[0]):
                    check_energy_level(new_x, new_y, m)

def part1(m, steps=100):
    flashes = 0
    for _ in range(steps):
        for y, line in enumerate(m):
            for x, _ in enumerate(line):
                check_energy_level(x, y, m)

        for y, line in enumerate(m):
            for x, _ in enumerate(line):
                if type(m[y][x]) is bool:
                    m[y][x] = 0
                    flashes += 1

    return flashes

def part2(m):
    for s in range(1000):
        m_copied = copy.deepcopy(m)
        part1(m_copied, s)
        if sum(map(sum, m_copied)) == 0:
            return s

    return -1


with open("input.txt") as f:
    text = f.read()

m = text.splitlines()
m = list(map(lambda x: list(map(int, list(x))), m))

print(f"part1: {part1(copy.deepcopy(m))}")
print(f"part2: {part2(m)}")
