import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

chunks = input().split()

ans = ""

for chunk in chunks:
    for key, value in {"sp": " ", "bS": "\\", "sQ": "'"}.items():
        chunk = chunk.replace(key, value)

    if chunk == "nl":
        ans += "\n"
    else:
        c = chunk[-1]
        n = int(chunk[:-1])
        ans += c*n

print(ans)
