from aocd import data
from scipy import sparse

ROTATION_COST = 1000
MOVE_COST = 1

tile_types = {
    (i, j): c
    for j, row in enumerate(data.splitlines())
    for i, c in enumerate(row)
}
open_tiles = {pos for pos, t in tile_types.items() if t != "#"}
start = next(pos for pos, t in tile_types.items() if t == "S")
end = next(pos for pos, t in tile_types.items() if t == "E")

circle = [
    (1, 0),  # east
    (0, 1),  # north
    (-1, 0),  # west
    (0, -1),  # south
]
graph = [
    (
        (i, j, di, dj),
        (i, j, di2, dj2),
        ROTATION_COST,
    )
    for i, j in open_tiles
    for di, dj in circle
    for di2, dj2 in circle
    if abs(di) != abs(di2)  # only include perpendicular, and we're in C4
] + [
    (
        (i, j, di, dj),
        (i + di, j + dj, di, dj),
        MOVE_COST,
    )
    for i, j in open_tiles
    for di, dj in circle
    if (i + di, j + dj) in open_tiles
]


def make_1d(i, j, di, dj):  # obviously slightly silly :)
    return i + 1000 * j + 1_000_000 * circle.index((di, dj))


# could just construct sparse matrix directly if desired
pt0s = []
pt1s = []
weights = []
for pt0, pt1, weight in graph:
    pt0s.append(make_1d(*pt0))
    pt1s.append(make_1d(*pt1))
    weights.append(weight)
sparse_mat = sparse.coo_matrix((weights, (pt0s, pt1s)))
dijkstra_res = sparse.csgraph.dijkstra(
    sparse_mat,
    indices=make_1d(*start, 1, 0),  # start facing east
)
results = [
    dijkstra_res[make_1d(*end, di, dj)]  # end in any orientation:
    for di, dj in circle
]
print(min(results))
