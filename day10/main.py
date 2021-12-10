#!/usr/bin/env python

def check(line):
    openings = ["(", "[", "{", "<"]
    closings = [")", "]", "}", ">"]
    points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    stack = []
    for c in line:
        if c in openings:
            stack.append(closings[openings.index(c)])
        else:
            if c != stack.pop():
                return points[c]

    return 0

def part1(lines):
    return sum(map(check, lines))

def complete(line):
    openings = ["(", "[", "{", "<"]
    closings = [")", "]", "}", ">"]
    points = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }
    stack = []
    for c in line:
        if c in openings:
            stack.append(closings[openings.index(c)])
        else:
            stack.pop()
    
    r = 0
    for c in reversed(stack):
        r = r * 5
        r = r + points[c]

    return r

def part2(lines):
    incomplete = []
    for l in lines:
        if check(l) == 0:
            incomplete.append(l)
    
    scores = list(map(complete, incomplete))
    scores.sort()
    return scores[len(scores) // 2]

with open("input.txt") as f:
    text = f.read()

lines = text.splitlines()

print(f"part1: {part1(lines)}")
print(f"part2: {part2(lines)}")
