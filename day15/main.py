#!/usr/bin/env python

from queue import PriorityQueue

def part1(m):
    h, w = len(m), len(m[0])
        
    pq = PriorityQueue()
    pq.put((0, (0, 0)))
    visited = {(0, 0),}

    while pq:
        curr_weight, (x, y) = pq.get()

        if x == w - 1 and y == h - 1:
            return curr_weight

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x = x - dx
            new_y = y - dy
            if 0 <= new_x < w and 0 <= new_y < h and (new_x, new_y) not in visited:
                weight = m[new_y][new_x]
                pq.put((curr_weight + weight, (new_x, new_y)))
                visited.add((new_x, new_y))

    return -1

def part2(m):
    h = len(m)
    new_m = []
    for y in range(h * 5):
        new_row = []
        for n in range(5):
            new_row += map(lambda x: (x + y // h + n - 1) % 9 + 1, m[y % h])
        new_m.append(new_row)

    return part1(new_m)

with open("input.txt") as f:
    m = [list(map(int, line)) for line in f.read().splitlines()]

print(f"part1: {part1(m)}")
print(f"part2: {part2(m)}")
