import sys
import math

def apply_rotor(rotor, message):
    new_message = ""
    for letter in message:
        new_message += rotor[abc.find(letter)]

    # print(rotor)
    # print(new_message)
    return new_message

def apply_reverse_rotor(rotor, message):
    new_message = ""
    for letter in message:
        new_message += abc[rotor.find(letter)]

    # print(rotor)
    # print(new_message)
    return new_message

def apply_caesar(shift, message):
    new_message = ""
    for letter in message:
        # print(f"{shift=}", file=sys.stderr, flush=True)
        rotor = abc[shift:]+abc[:shift]
        new_message += rotor[abc.find(letter)]
        # print(f"c{rotor=}", file=sys.stderr, flush=True) # print(rotor)

        shift = shift+1 if shift < 25 else 0

    # print(f"{new_message=}", file=sys.stderr, flush=True) # print(new_message)
    return new_message

def apply_reverse_caesar(shift, message):
    new_message = ""
    for letter in message:
        # print(f"{shift=}", file=sys.stderr, flush=True)
        rotor = abc[shift:]+abc[:shift]
        new_message += abc[rotor.find(letter)]
        # print(f"c{rotor=}", file=sys.stderr, flush=True) # print(rotor)

        shift = shift+1 if shift < 25 else 0

    # print(f"{new_message=}", file=sys.stderr, flush=True) # print(new_message)
    return new_message

rotors = []
operation = input()
prn = int(input())
for i in range(3):
    rotors.append(input()) 

message = input()
# print(f"{message=}",file=sys.stderr,flush=True)

abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if operation == "ENCODE":
    # print("ENCODE", file=sys.stderr, flush=True)
    message = apply_caesar(prn, message)
    # print(f"{message=}", file=sys.stderr, flush=True)
    for rotor in rotors:
        # print(f"{rotor=}", file=sys.stderr, flush=True)
        message = apply_rotor(rotor, message)
        # print(f"{message=}", file=sys.stderr, flush=True)

if operation == "DECODE":
    # print("DECODE", file=sys.stderr, flush=True)
    for rotor in reversed(rotors):
        # print(f"{rotor=}", file=sys.stderr, flush=True)
        message = apply_reverse_rotor(rotor, message)
        # print(f"{message=}", file=sys.stderr, flush=True)

    message = apply_reverse_caesar(prn, message)

print(f"{message}")