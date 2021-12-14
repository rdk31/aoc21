#!/usr/bin/env python

from collections import Counter

def grow(pairs, rules):
    for k, v in list(pairs.items()):
        r = rules[k]
        if k[0] + r not in pairs:
            pairs[k[0] + r] = v
        else:
            pairs[k[0] + r] += v

        if r + k[1] not in pairs:
            pairs[r + k[1]] = v
        else:
            pairs[r + k[1]] += v

        pairs[k] -= v
        if pairs[k] < 1:
            del pairs[k]

    return pairs

def solve(template, rules, steps):
    pairs = [template[i:i+2] for i in range(len(template) - 1)]
    pairs = {x:pairs.count(x) for x in set(pairs)}

    for _ in range(steps):
        pairs = grow(pairs, rules)

    c = Counter()
    for (k, v) in pairs.items():
        c[k[0]] += v
    c[template[-1]] += 1
    most_common = c.most_common()

    return most_common[0][1] - most_common[-1][1]

with open("input.txt") as f:
    text = f.read()

split = text.split("\n\n")
template = split[0]
rules = dict(item.split(" -> ") for item in split[1].splitlines())

print(f"part1: {solve(template, rules, 10)}")
print(f"part2: {solve(template, rules, 40)}")
