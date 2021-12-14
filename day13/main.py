#!/usr/bin/env python

def fold(dots, x=None, y=None):
    assert x is not None or y is not None
    new_dots = []
    for (dot_x, dot_y) in dots:
        if x:
            if dot_x > x:
                new_dots.append((dot_x - 2 * (dot_x - x), dot_y))
            else:
                new_dots.append((dot_x, dot_y))
        elif y:
            if dot_y > y:
                new_dots.append((dot_x, dot_y - 2 * (dot_y - y)))
            else:
                new_dots.append((dot_x, dot_y))
    
    return set(new_dots)

def part1(dots, folds):
    f = folds[0].split("=")
    f = {
        f[0]: int(f[1])
    }
    new_dots = fold(dots, **f)
    return len(new_dots)

def part2(dots, folds):
    new_dots = dots
    for f in folds:
        f = f.split("=")
        f = {
            f[0]: int(f[1])
        }
        new_dots = fold(new_dots, **f)

    max_x = max(map(lambda x: x[0], new_dots)) + 1
    max_y = max(map(lambda x: x[1], new_dots)) + 1

    print("part2:")
    for y in range(max_y):
        for x in range(max_x):
            if (x, y) in new_dots:
                print("X", end="")
            else:
                print(" ", end="")

        print()

with open("input.txt") as f:
    text = f.read()

split = text.split("\n\n")
dots = list(map(lambda x: tuple(map(int, x.split(","))),split[0].splitlines()))
folds = list(map(lambda x: x[11:], split[1].splitlines()))

print(f"part1: {part1(dots, folds)}")
part2(dots, folds)
