#!/usr/bin/env python

def solve(board, moves):
    marked = []
    total_sum = sum(map(sum, board))

    for i, move in enumerate(moves):
        for y, row in enumerate(board):
            for x, num in enumerate(row):
                if num == move:
                    total_sum -= num
                    marked.append((x, y))

        for x in range(5):
            vertical = [m for m in marked if m[0] == x]
            horizontal = [m for m in marked if m[1] == x]
            if len(vertical) == 5 or len(horizontal) == 5:
                return i, total_sum * move

    return -1, -1

if __name__ == "__main__":
    with open("input.txt") as f:
        text = f.read()

    lines = text.splitlines()

    moves = list(map(lambda x: int(x), lines[0].split(",")))
    boards = []

    board = []
    for line in lines[2:]:
        if line:
            board.append(list(map(lambda x: int(x), line.split())))
        else:
            boards.append(board)
            board = []
    boards.append(board)

    move_min = len(moves)
    move_max = 0
    top_score = 0
    worst_score = 0
    for board in boards:
        move_num, score = solve(board, moves)
        if move_min > move_num:
            move_min = move_num
            top_score = score

        if move_max < move_num:
            move_max = move_num
            worst_score = score

    print(f"part1: {top_score}")
    print(f"part2: {worst_score}")
