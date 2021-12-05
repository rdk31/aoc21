#!/usr/bin/env python

def filter_vertical_and_horizontal(lines):
    for line in lines:
        if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            yield line

def get_points(line):
    dx = line[1][0] - line[0][0]
    dy = line[1][1] - line[0][1]
    if dx == 0:
        for y in range(abs(dy) + 1):
            if dy < 0:
                yield (line[0][0], line[0][1] - y)
            else:
                yield (line[0][0], line[0][1] + y)
    elif dy == 0:
        for x in range(abs(dx) + 1):
            if dx < 0:
                yield (line[0][0] - x, line[0][1])
            else:
                yield (line[0][0] + x, line[0][1])
    else:
        for d in range(abs(dx) + 1):
            yield (line[0][0] + dx/abs(dx) * d, line[0][1] + dy/abs(dy) * d)

def part1(lines):
    seen = {}

    for l in lines:
        for p in get_points(l):
            if p in seen:
                seen[p] += 1
            else:
                seen[p] = 1

    return len([k for k, v in seen.items() if v > 1])

if __name__ == "__main__":
    with open("input.txt") as f:
        text = f.read()

    l = text.splitlines()
    
    lines = []
    for line in l:
        points = line.split(" -> ")
        points = list(map(lambda x: x.split(","), points))
        points = ((int(points[0][0]), int(points[0][1])), (int(points[1][0]), int(points[1][1])))
        lines.append(points)

    print(f"part1: {part1(filter_vertical_and_horizontal(lines))}")
    print(f"part2: {part1(lines)}")

