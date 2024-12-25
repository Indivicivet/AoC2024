from aocd import data
from scipy import sparse

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


def make_1d(i, j, di, dj):  # obviously slightly silly :)
    return i + 1000 * j + 1_000_000 * circle.index((di, dj))


# could just construct sparse matrix directly if desired
pt0s = []
pt1s = []
weights = []
for pt0, pt0_neighbours in graph.items():
    for pt1, weight in pt0_neighbours:
        pt0s.append(make_1d(*pt0))
        pt1s.append(make_1d(*pt1))
        weights.append(weight)
sparse_mat = sparse.coo_matrix((weights, (pt0s, pt1s)))
left = min(i for i, _ in open_tiles)
bottom = max(j for _, j in open_tiles)
right = max(i for i, _ in open_tiles)
top = min(j for _, j in open_tiles)
print(open_tiles)
dijkstra_res = sparse.csgraph.dijkstra(
    sparse_mat,
    indices=make_1d(21, 6, 1, 0),  # start facing east
)
results = [
    dijkstra_res[make_1d(21, 6, di, dj)]
    for di, dj in circle
]
print(results)
