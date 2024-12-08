import numpy as np
from aocd import data
from collections import defaultdict

print(data)

nodes = defaultdict(list)
for j, row in enumerate(data.splitlines()):
    for i, val in enumerate(row):
        nodes[val].append((j, i))

total_antinodes = 0
antinodes = defaultdict(lambda: np.array([len("..........................................U.......")]*2))
for key, positions in nodes.items():
    for key2, positions2 in nodes.items():
        if key != key2:
            continue
        if key == ".":
            continue
        for position in positions:
            for position2 in positions2:
                offs_x = position2[1] - position[1]
                offs_y = position2[0] - position[0]
                antinodes[(position2[0] + offs_y, position2[1] + offs_x)] = 1
print(sum(np.sum(anvals) for anvals in antinodes.values()))

