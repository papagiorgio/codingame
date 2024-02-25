import sys
import math


def quersumme(n):
    s = str(n)
    sum=0
    for i in s:
        sum += int(i)

    return sum

def count(table, t):
    print(f"rec {table}", file=sys.stderr, flush=True)

    if len(table)==1:
        return 1 if table[0][0] <= t else 0
    elif table[0][0] > t:
        return 0
    else:
        return 2 + count([x[1:] for x in table[1:]], t)
    
def get_neighbors(i, j, r, c, table):
    neighbors = []
    if i > 0 and table[i-1][j]:
        neighbors.append((i-1, j))
    if i < r-1 and table[i+1][j]:
        neighbors.append((i+1, j))
    if j > 0 and table[i][j-1]:
        neighbors.append((i, j-1))
    if j < c-1 and table[i][j+1]:
        neighbors.append((i, j+1))
    return neighbors
        
def bfs(graph, start): # get the size of the connected component in the graph
    explored = []

    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                queue.append(neighbour)
            explored.append(node)
    
    return len(explored)

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r = int(input())
c = int(input())
t = int(input())
print(f"{c=}, {r=}, {t=}", file=sys.stderr, flush=True)

sum = 0

table = [[True if (quersumme(i)+quersumme(j)<=t) else False for i in range(c)] for j in range(r)]

graph = {}

for i in range(r):
    for j in range(c):
        if table[i][j]:
            graph[(i,j)] = get_neighbors(i, j, r, c, table)

sum = bfs(graph, (0,0))

print(f"{graph= }", file=sys.stderr, flush=True)

# [print(f"{c= }", file=sys.stderr, flush=True) for c in graph.values()]


# Write an answer using print
print(f"{table= }", file=sys.stderr, flush=True)
# tmp = [x[1:] for x in table[1:]]
#print(f"{quersumme(23)=}", file=sys.stderr, flush=True)

# for row in table:
#     for col in row:
#         # print(f"{col= }", file=sys.stderr, flush=True)
#         if col <= t:
#             sum+=1
#         else: 
#             break

# for i in range(c):
#     for j in range(r):
#         print(f"{i= }, {j=}", file=sys.stderr, flush=True)

#         print(f"{table[i][j]}", file=sys.stderr, flush=True)

#         if table[i][j] <= t:
#             sum+=1

print(sum)
