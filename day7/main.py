#!/usr/bin/env python

with open("input.txt") as f:
    l = f.readline()

pos = list(map(int, l.split(",")))

min_s = None

for i in range(max(pos) + 1):
    s = 0
    for p in pos:
        s += abs(p - 1)

    if not min_s or s < min_s:
        min_s = s

print(f"part1: {min_s}")

min_s = None

for i in range(max(pos) + 1):
    s = 0
    for p in pos:
        ds = abs(p - i)
        s += (ds + 1) * ds / 2

    if not min_s or s < min_s:
        min_s = s

print(f"part2: {min_s}")
