import sys
import math

POINTS = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1, "m": 3,
          "n": 1, "o": 1, "p": 3, "q": 10, "r": 1, "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8, "y": 4, "z": 10}

n = int(input())
words = []
scores = []

for i in range(n):
    words.append(input())
    
letters = input()

print(f"{n=}, {words=}, {letters=}", file=sys.stderr, flush=True)

for word in words:
    score = 0
    tmp_letters = letters
    for letter in word:
        # print(f"{word=}", file=sys.stderr, flush=True)

        if letter in tmp_letters:
            tmp_letters = tmp_letters.replace(letter, "", 1)
            score += POINTS[letter]
        else:
            score = 0
            break
    scores.append(score)
    # print(f"{word=}: {score=}", file=sys.stderr, flush=True)
# print(f"{scores=}", file=sys.stderr, flush=True)

print(f"{words[(scores.index(max(scores)))]}")

