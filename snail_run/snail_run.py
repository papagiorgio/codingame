import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

number_snails = int(input())

speed_snails = [int(input()) for _ in range(number_snails)]

map_height = int(input())
map_width = int(input())

grid = [input() for i in range(map_height)]
print(f"{grid=}", file=sys.stderr, flush=True)
print(f"{speed_snails=}" , file=sys.stderr, flush=True)

# get a list of coordinates for the targets (#) from the grid
targets = []
for i in range(map_height):
    for j in range(map_width):
        if grid[i][j] == "#":
            targets.append((i, j))

print(f"{targets=}", file=sys.stderr, flush=True)

# get a list of coordinates for the snails (s1 to snumber_snails) from the grid
snail_coordinates = [None] * number_snails
for i in range(map_height):
    for j in range(map_width):
        for k in range(number_snails):
            if grid[i][j] == f"{k+1}":
                snail_coordinates[k] = (i, j)

print(f"{snail_coordinates=}", file=sys.stderr, flush=True)

# get the length of the shortest path from each snail to the nearest target and divide each path by the speed of the snail
shortest_paths = []
for snail in snail_coordinates:
    distances = []
    for target in targets:
        distances.append(math.sqrt((snail[0]-target[0])**2 + (snail[1]-target[1])**2))
    print(f"{distances=}", file=sys.stderr, flush=True)
    shortest_paths.append(min(distances)/speed_snails[snail_coordinates.index(snail)])

print(f"{shortest_paths=}", file=sys.stderr, flush=True)

# get the snail that reaches the nearest target first
fastest_snail = shortest_paths.index(min(shortest_paths))+1

print(fastest_snail)
