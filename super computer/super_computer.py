import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
count = 1
n = int(input())
requests = []
for i in range(n):
    j, d = [int(j) for j in input().split()]
    requests.append((j, j+d-1))

requests.sort(key=lambda x: x[1])
current_end_time = requests[0][1]

for request in requests:
    if request[0] > current_end_time:
        count += 1
        current_end_time = request[1]

print(count)
