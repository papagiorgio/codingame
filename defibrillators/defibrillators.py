import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

u_lon = float(input().replace(",", ".")) * math.pi / 180
u_lat = float(input().replace(",", ".")) * math.pi / 180
n = int(input())
defibs = []


for i in range(n):
    _, name, _, _, d_lon, d_lat = input().split(";")
    d_lon = float(d_lon.replace(",", ".")) * math.pi / 180
    d_lat = float(d_lat.replace(",", ".")) * math.pi / 180
    defibs.append((name, d_lon, d_lat))
    print(f"{name=}", file=sys.stderr, flush=True)
    print(f"{d_lon=}", file=sys.stderr, flush=True)
    print(f"{d_lat=}", file=sys.stderr, flush=True)

# print(f"{defibs=}", file=sys.stderr, flush=True)

min_defib = None
min_d = math.inf

for defib in defibs:
    x = (u_lon - defib[1]) * math.cos(u_lat + defib[2]) / 2
    y = u_lat - defib[2]
    d = math.sqrt(x**2 + y**2) * 6371
    if d < min_d:
        min_d = d
        min_defib = defib

print(min_defib[0])