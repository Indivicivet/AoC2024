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
graph = {
    (i, j, di, dj): [  # rotations; two possible
        ((i, j, di2, dj2), ROTATION_COST)
        for di2, dj2 in circle
        if abs(di) != abs(di2)  # only include perpendicular, and we're in C4
    ]
    + (  # move option - only one possibility
        [((i + di, j + dj, di, dj), MOVE_COST)]
        if (i + di, j + di) in open_tiles
        else []
    )
    for i, j in open_tiles
    for di, dj in circle
}

print(graph)
# todo :: now we djikstra
