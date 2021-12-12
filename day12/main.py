#!/usr/bin/env python

def part1_(conns, start, end, routes, route=[]):
    route.append(start)
    for n in conns[start]:
        if n.islower() and n in route:
            continue

        if n == end:
            ret = route.copy()
            ret.append(n)
            routes.append(ret)
        else:
            part1_(conns, n, end, routes, route.copy())

def part1(conns):
    routes = []
    part1_(conns, "start", "end", routes)
    return len(routes)

def part2_(conns, start, end, routes, route=[]):
    route.append(start)
    for n in conns[start]:
        if n in ["start", "end"] and n in route:
            continue

        if n.islower():
            c = route.copy()
            c.append(n)
            small = {x:c.count(x) for x in set(c) if x.islower()}
            one = len(list(filter(lambda x: x == 2, small.values())))
            none = len(list(filter(lambda x: x > 2, small.values())))
            if one > 1 or none > 0:
                continue

        if n == end:
            ret = route.copy()
            ret.append(n)
            routes.append(ret)
        else:
            part2_(conns, n, end, routes, route.copy())

def part2(conns):
    routes = []
    part2_(conns, "start", "end", routes)
    return len(routes)

with open("input.txt") as f:
    text = f.read()

conns = {}
for c in list(map(lambda x: x.split("-"), text.splitlines())):
    if c[0] not in conns:
        conns[c[0]] = [c[1]]
    else:
        conns[c[0]].append(c[1])
    if c[1] not in conns:
        conns[c[1]] = [c[0]]
    else:
        conns[c[1]].append(c[0])

print(f"part1: {part1(conns)}")
print(f"part2: {part2(conns)}")
