from aocd import data
import numpy as np
from PIL import Image
from tqdm import tqdm


WIDTH = 101
HEIGHT = 103

GRID_MAJOR = 10
GRID_MINOR = 5


def tile_getter():
    robots = []
    for txt_line in data.splitlines():
        p_str, v_str = txt_line[2:].split(" v=")
        px, py = map(int, p_str.split(","))
        vx, vy = map(int, v_str.split(","))
        robots.append(
            (
                np.array([px, py]),
                np.array([vx, vy]),
            )
        )
    for i in range(9999999999):
        # viz
        arr = np.zeros((HEIGHT, WIDTH), dtype=np.uint8)
        if i % GRID_MINOR == 0 or (i // GRID_MINOR) % GRID_MINOR == 0:
            arr[...] = 8
        if i % GRID_MAJOR == 0 or (i // GRID_MAJOR) % GRID_MAJOR == 0:
            arr[...] = 16
        arr[0, ...] = 32
        arr[..., 0] = 32
        for (px, py), _ in robots:
            arr[py, px] = 255
        yield arr
        # timestep
        for pos, vel in robots:
            pos += vel  # mutable
            pos %= [WIDTH, HEIGHT]


tile = tile_getter()

H_TILES = 70
V_TILES = 50
assert H_TILES % GRID_MAJOR == 0  # for the print
assert V_TILES % GRID_MAJOR == 0
assert H_TILES * V_TILES * 3 >= WIDTH * HEIGHT

tiles = np.dstack([
    np.vstack([
        np.hstack([
            next(tile)
            for _ in range(H_TILES)
        ])
        for _ in tqdm(range(V_TILES))
    ])
    for _ in tqdm(range(3))
])
Image.fromarray(tiles).show()

c = "rgb".index(input("colour [rgb]? ").lower())

i = int(input("column? "))
j = int(input("row?" ))
print((c * H_TILES * V_TILES + j * H_TILES + i) % (H_TILES * V_TILES * 3))
