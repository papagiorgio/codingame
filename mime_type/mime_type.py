import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n_elements = int(input())  # Number of elements which make up the association table.
n_names = int(input())  # Number Q of file names to be analyzed.

mime_dict = {}

for i in range(n_elements):
    ext, mt = input().split()
    mime_dict[ext.lower()] = mt

for i in range(n_names):
    fname = input()  # One file name per line.
    ext = fname.split('.')[-1].lower()
    
    if fname != ext and ext in mime_dict:
        print(mime_dict[ext])
    else:
        print("UNKNOWN")