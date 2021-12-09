#!/usr/bin/env python

# top - 1; right - 2; down - 3; left - 4
def lowest(x, y, m, ignore_dir=0):
    v = m[y][x]
    max_y = len(m) - 1
    max_x = len(m[0]) - 1
    if x > 0 and ignore_dir != 4:
        if m[y][x - 1] <= v:
            return False

    if x < max_x and ignore_dir != 2:
        if m[y][x + 1] <= v:
            return False

    if y > 0 and ignore_dir != 1:
        if m[y - 1][x] <= v:
            return False

    if y < max_y and ignore_dir != 3:
        if m[y + 1][x] <= v:
            return False

    return True

def part1(m):
    low_points = []
    for y, row in enumerate(m):
        for x, v in enumerate(row):
            if lowest(x, y, m):
                low_points.append(v)

    return sum(map(lambda x: x + 1, low_points))

# top - 1; right - 2; down - 3; left - 4
def part2_(x, y, m, ignore_dir=0):
    basin = []

    max_y = len(m) - 1
    max_x = len(m[0]) - 1
    if x > 0 and ignore_dir != 4:
        if m[y][x - 1] != 9 and m[y][x - 1] > m[y][x]:
            basin.append((x - 1, y))
            basin += part2_(x - 1, y, m, ignore_dir=2)

    if x < max_x and ignore_dir != 2:
        if m[y][x + 1] != 9 and m[y][x + 1] > m[y][x]:
            basin.append((x + 1, y))
            basin += part2_(x + 1, y, m, ignore_dir=4)

    if y > 0 and ignore_dir != 1:
        if m[y - 1][x] != 9 and m[y - 1][x] > m[y][x]:
            basin.append((x, y - 1))
            basin += part2_(x, y - 1, m, ignore_dir=3)

    if y < max_y and ignore_dir != 3:
        if m[y + 1][x] != 9 and m[y + 1][x] > m[y][x]:
            basin.append((x, y + 1))
            basin += part2_(x, y + 1, m, ignore_dir=1)
    
    return basin

def part2(m):
    basins = []
    for y, row in enumerate(m):
        for x, _ in enumerate(row):
            if lowest(x, y, m):
                basin = part2_(x, y, m)
                basin.append((x, y))
                basins.append(basin)

    lens = list(map(lambda b: len(set(b)), basins))
    lens.sort(reverse=True)
    r = 1
    for l in lens[:3]:
        r = r * l 

    return r

with open("input.txt") as f:
    text = f.read()

m = text.splitlines()
m = list(map(lambda x: list(map(int, list(x))), m))

print(f"part1: {part1(m)}")
print(f"part2: {part2(m)}")
