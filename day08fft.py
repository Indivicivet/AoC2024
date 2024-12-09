"""
can you do day8 with fourier transforms...?
"""

import numpy as np
from aocd import data
from collections import defaultdict

print(data)

LEN = len(data.splitlines()[0])
LENY = len(data.splitlines())

nodes = defaultdict(lambda: np.zeros((LENY, LEN)))
for j, row in enumerate(data.splitlines()):
    for i, val in enumerate(row):
        if val != ".":
            nodes[val][j, i] = 1

for part2 in [False, True]:
    antinodes = np.zeros([LENY, LEN], dtype=int)
    for key, arr in nodes.items():
        fourier = np.fft.fft2(arr)
        # TODO
        print(fourier)
    print(np.sum(antinodes))
