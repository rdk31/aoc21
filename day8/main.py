#!/usr/bin/env python

def part1(lines):
    a = {
        2: 1,
        4: 4,
        3: 7,
        7: 8
    }

    digits = [0] * 10

    for line in lines:
        split = line.split(" | ")

        for s in split[1].split(" "):
            if len(s) in a:
                digits[a[len(s)]] += 1
        
    print(f"part1: {sum(digits)}")

def decode(line):
    decoded = {str(i): None for i in range(10)}

    split = line[0].split(" ")
    for s in split:
        if len(s) == 2:
            decoded["1"] = s
        elif len(s) == 3:
            decoded["7"] = s
        elif len(s) == 4:
            decoded["4"] = s
        elif len(s) == 7:
            decoded["8"] = s

    for s in split:
        if len(s) == 6:
            if len(set(decoded["1"]) - set(s)) != 0:
                decoded["6"] = s
            elif len(set(decoded["4"]) - set(s)) == 0:
                decoded["9"] = s
            else:
                decoded["0"] = s

    b_segment = (set(decoded["1"]) - set(decoded["6"])).pop()
    for s in split:
        if len(s) == 5:
            if len(set(decoded["1"]) - set(s)) == 0:
                decoded["3"] = s
            elif b_segment in s:
                decoded["2"] = s
            else:
                decoded["5"] = s
  
    decoded = {frozenset(v):k for (k, v) in decoded.items()}
    return int("".join([decoded[frozenset(s)] for s in line[1].split(" ")]))

def part2(lines):
    s = 0
    for line in lines:
        split = line.split(" | ")
        s += decode(split)

    print(f"part2: {s}")

with open("input.txt") as f:
    lines = f.read()
lines = lines.splitlines()

part1(lines) 
part2(lines)
