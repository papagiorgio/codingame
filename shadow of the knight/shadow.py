import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
curr_x = x0
curr_y = y0
min_x = 0
min_y = 0
max_x = w-1
max_y = h-1

print(f"{w=}, {h=}, {n=}, {x0=}, {y0=}", file=sys.stderr, flush=True)

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    x = curr_x
    y = curr_y

    match bomb_dir:
        case "U":
            y = y - math.ceil((y-min_y)/2)
            max_y = curr_y
        case "D":
            y = y + math.ceil((max_y-y)/2)
            min_y = curr_y
        case "R":
            x = x + math.ceil((max_x-x)/2)
            min_x = curr_x
        case "L":
            x = x - math.ceil((x-min_x)/2)
            max_x = curr_x
        case "UR":
            x = x + math.ceil((max_x-x)/2)
            y = y - math.ceil((y-min_y)/2)
            max_y = curr_y
            min_x = curr_x
        case "DR":
            x = x + math.ceil((max_x-x)/2)
            y = y + math.ceil((max_y-y)/2)
            min_y = curr_y
            min_x = curr_x
        case "DL":
            x = x - math.ceil((x-min_x)/2)
            y = y + math.ceil((max_y-y)/2)
            min_y = curr_y
            max_x = curr_x
        case "UL":
            x = x - math.ceil((x-min_x)/2)
            y = y - math.ceil((y-min_y)/2)
            max_y = curr_y
            max_x = curr_x

    curr_x = x
    curr_y = y
    # the location of the next window Batman should jump to.
    print(x, y)
