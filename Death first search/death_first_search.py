import sys
import math

def bfs_shortest_path(graph, start, goals):

    if start in goals:
        return [start]

    explored = []
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                if neighbour in goals:
                    return new_path
 
            explored.append(node)

    return None


def bfs_all_paths(graph, start, goals):
    paths = []

    if start in goals:
        paths.append([start])
        return paths
    
    explored = []
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour in goals:
                    paths.append(new_path)

            explored.append(node)

    return paths


def is_danger_path(path, fringe_nodes):
    for node in path[1:]:
        if node not in fringe_nodes:
            return False
    return True

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
exits = []
graph = {}
last_links = {}
fringe_nodes = []
danger_nodes = []

for i in range(l):
    v1, v2 = [j for j in input().split()]

    if v1 not in graph:
        graph[v1] = [v2]
    else:
        graph[v1].append(v2)

    if v2 not in graph:
        graph[v2] = [v1]
    else:
        graph[v2].append(v1)

for i in range(e):
    exits.append(input()) 

    for v in graph[exits[-1]]: 
        if v not in last_links:
            last_links[v] = [exits[-1]]
        else:
            last_links[v].append(exits[-1])
        if v not in fringe_nodes:
            fringe_nodes.append(v)

for k, v in last_links.items():
    if len(v) == 2:
        danger_nodes.append(k)

# game loop
while True:
    agent_position = input()  # The index of the node on which the Bobnet agent is positioned this turn

    shortest_path = bfs_shortest_path(graph, agent_position, exits)

    if len(shortest_path) > 2: # no immediate danger, look for a danger node and sever one of its links
        if len(danger_nodes)==1: # only one danger node left, go for it
            shortest_path = bfs_shortest_path(graph, agent_position, danger_nodes)
            node1 = shortest_path[-1]
            node2 = last_links[node1][0]
            danger_nodes.remove(node1)
            last_links[node1].remove(node2)
            print(f"{shortest_path= }, {node1= }, {node2= }", file=sys.stderr, flush=True)
        elif len(danger_nodes)>1: # more than one danger node left, 
              # check if there is a danger path (not neccessarily shortest) to any of them
                paths = bfs_all_paths(graph, agent_position, danger_nodes)
                danger = False
                for path in paths:
                    if is_danger_path(path, fringe_nodes): 
                        node1 = path[-1]
                        node2 = last_links[node1][0]
                        danger_nodes.remove(node1)
                        last_links[node1].remove(node2)
                        danger = True
                if not danger:
                    node1 = path[-1]
                    node2 = last_links[node1][0]
                    danger_nodes.remove(node1)
                    last_links[node1].remove(node2)
        else:
            node1 = shortest_path[-1]
            node2 = shortest_path[-2]

    else: # the agent wins if we don't sever the link
        node1 = shortest_path[-1]
        node2 = shortest_path[-2]

    print(f"{node1= }, {node2= }", file=sys.stderr, flush=True)

    graph[node1].remove(node2)
    graph[node2].remove(node1)

    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    print(f"{node1} {node2}")