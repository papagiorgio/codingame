import sys
import math

def move(x, y, dir):
    match dir:
        case "D":
            return (x, y + 1)
        case "R":
            return (x + 1, y)
        case "L":
            return (x - 1, y)
        case "DL":
            return (x - 1, y + 1)
        case "DR":
            return (x + 1, y + 1)
        

def get_out(grid, pos, x, y):
    print(f"{grid[y][x]=}", file=sys.stderr, flush=True)
    match grid[y][x]:
        case "1":
            match pos:
                case "TOP":
                    return move(x, y, "D")
                case "RIGHT":
                    return move(x, y, "D")
                case "LEFT":
                    return move(x, y, "D")
        case "2":
            match pos:
                case "RIGHT":
                    return move(x, y, "L")
                case "LEFT":
                    return move(x, y, "R")
        case "3":
            match pos:
                case "TOP":
                    return move(x, y, "D")
        case "4":
            match pos:
                case "TOP":
                    return move(x, y, "L")
                case "RIGHT":
                    return move(x, y, "D")
        case "5":
            match pos:
                case "TOP":
                    return move(x, y, "R")
                case "LEFT":
                    return move(x, y, "D")
        case "6":
            match pos:
                case "RIGHT":
                    return move(x, y, "L")
                case "LEFT":
                    return move(x, y, "R")
        case "7":
            match pos:
                case "TOP":
                    return move(x, y, "D")
                case "RIGHT":
                    return move(x, y, "D")
        case "8":
            match pos:
                case "RIGHT":
                    return move(x, y, "D")
                case "LEFT":
                    return move(x, y, "D")
        case "9":
            match pos:
                case "TOP":
                    return move(x, y, "D")
                case "LEFT":
                    return move(x, y, "D")
        case "10":
            match pos:
                case "TOP":
                    return move(x, y, "L")
        case "11":
            match pos:
                case "TOP":
                    return move(x, y, "R")
        case "12":
            match pos:
                case "RIGHT":
                    return move(x, y, "D")
        case "13":
            match pos:
                case "LEFT":
                    return move(x, y, "D")
        case _:
            return (x, y)

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

grid = []

# w: number of columns.
# h: number of rows.
w, h = [int(i) for i in input().split()]

print(f"{w=}, {h=}", file=sys.stderr, flush=True)

for i in range(h):
    line = input()  # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
    grid.append(line.split(" "))
ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

print(f"{grid=}", file=sys.stderr, flush=True)

# game loop
while True:
    inputs = input().split()
    xi = int(inputs[0])
    yi = int(inputs[1])
    pos = inputs[2]

    print(f"{xi=}, {yi=}, {pos=}", file=sys.stderr, flush=True)

    print(f"{get_out(grid, pos, xi, yi)=}", file=sys.stderr, flush=True)

    x_out, y_out = get_out(grid, pos, xi, yi)

    print(f"{grid[xi][yi]=}:", file=sys.stderr, flush=True)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
    print(f"{x_out} {y_out}")
