from collections import defaultdict

from aocd import data

ROTATION_COST = 1000
MOVE_COST = 1

open_tiles = {
    (i, j)
    for j, row in enumerate(data.splitlines())
    for i, c in enumerate(row)
    if c == "."
}
circle = [
    (1, 0),  # east
    (0, 1),  # north
    (-1, 0),  # west
    (0, -1),  # south
]
graph = defaultdict(list)  # node A -> [(node B, cost)]
for i, j in open_tiles:
    for di, dj in circle:
        first = (i, j, di, dj)
        for di2, dj2 in circle:
            if abs(di) != abs(di2):  # only include perpendicular, and we're in C4
                graph[first].append(((i, j, di2, dj2), ROTATION_COST))
        i2 = i + di
        j2 = j + dj
        if (i2, j2) in open_tiles:
            graph[first].append(((i2, j2, di, dj), MOVE_COST))

print(graph)
# todo :: now we djikstra
