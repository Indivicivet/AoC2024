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
    for key in nodes:
        if key == ".":
            continue
        for x0, y0 in nodes[key]:
            for x1, y1 in nodes[key]:
                offs_x = x1 - x0
                offs_y = y1 - y0
                if not (offs_x or offs_y):
                    continue
                for offs_rel_pos in range(-LEN-1, LEN+1) if part2 else [-1, 2]:
                    harm_x = x0 + offs_x * offs_rel_pos
                    harm_y = y0 + offs_y * offs_rel_pos
                    if harm_x < 0 or harm_y < 0 or harm_y >= LENY or harm_x >= LEN:
                        continue
                    antinodes[harm_y, harm_x] = 1
    print(np.sum(antinodes))
