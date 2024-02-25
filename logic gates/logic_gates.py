import sys
import math

n = int(input())
m = int(input())

inputs = {}
outputs = {}

for i in range(n):
    input_name, input_signal = input().split()
    inputs[input_name] = input_signal

print(f"{inputs=}", file=sys.stderr, flush=True)

for i in range(m):
    output_name, _type, input_name_1, input_name_2 = input().split()
    print(f"{output_name=}, {_type=}, {input_name_1=}, {input_name_2=}", file=sys.stderr, flush=True)
    outputs[output_name] = ""
    if _type == "AND":
        for i in range(len(inputs[input_name_1])):
            if inputs[input_name_1][i] == "_" or inputs[input_name_2][i] == "_":
                outputs[output_name] += "_"
            else:
                outputs[output_name] += "-"
    elif _type == "OR":
        for i in range(len(inputs[input_name_1])):
            if inputs[input_name_1][i] == "-" or inputs[input_name_2][i] == "-":
                outputs[output_name] += "-"
            else:
                outputs[output_name] += "_"  
    elif _type == "XOR":
        for i in range(len(inputs[input_name_1])):
            if inputs[input_name_1][i] == inputs[input_name_2][i]:
                outputs[output_name] += "_"
            else:
                outputs[output_name] += "-"
    elif _type == "NAND":
        for i in range(len(inputs[input_name_1])):
            if inputs[input_name_1][i] == "-" and inputs[input_name_2][i] == "-":
                outputs[output_name] += "_"
            else:
                outputs[output_name] += "-"
    elif _type == "NOR":
        for i in range(len(inputs[input_name_1])):
            if inputs[input_name_1][i] == "_" and inputs[input_name_2][i] == "_":
                outputs[output_name] += "-"
            else:
                outputs[output_name] += "_"
    elif _type == "NXOR":
        for i in range(len(inputs[input_name_1])):
            if inputs[input_name_1][i] == inputs[input_name_2][i]:
                outputs[output_name] += "-"
            else:
                outputs[output_name] += "_"

# print(f"{inputs=}")
[print(f"{k} {v}") for k, v in outputs.items()]