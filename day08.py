import numpy as np
from aocd import data
from collections import defaultdict

print(data)

nodes = defaultdict(list)
for j, row in enumerate(data.splitlines()):
    for i, val in enumerate(row):
        nodes[val].append((j, i))

LEN = len(data.splitlines()[0])
LENY = len(data.splitlines())
total_antinodes = 0
antinodes = defaultdict(lambda: np.array([LEN]*2))
for key, positions in nodes.items():
    for key2, positions2 in nodes.items():
        if key != key2:
            continue
        if key == ".":
            continue
        for position in positions:
            for position2 in positions2:
                if position == position2:
                    continue
                offs_x = position2[1] - position[1]
                offs_y = position2[0] - position[0]
                for harm in [
                    (position2[0] + offs_y, position2[1] + offs_x),
                    (position[0] - offs_y, position[1] - offs_x),
                ]:
                    if harm[0] < 0 or harm[1] < 0 or harm[0] >= LENY or harm[1] >= LEN:
                        continue
                    antinodes[harm] = 1
print(sum(np.sum(anvals) for anvals in antinodes.values()))

