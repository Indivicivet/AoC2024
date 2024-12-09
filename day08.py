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

for part2 in [False, True]:
    antinodes = np.zeros([LENY, LEN], dtype=int)
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
                    for offs_rel_pos in range(-LEN-1, LEN+1) if part2 else [-1, 2]:
                        harm_x = position[0] + offs_y * offs_rel_pos
                        harm_y = position[1] + offs_x * offs_rel_pos
                        if harm_x < 0 or harm_y < 0 or harm_y >= LENY or harm_x >= LEN:
                            continue
                        antinodes[harm_y, harm_x] = 1
    print(np.sum(antinodes))
