from collections import defaultdict

from aocd import data
import numpy as np

WIDTH = 101
HEIGHT = 103
TIME_STEPS = 100

quads = defaultdict(int)
for txt_line in data.splitlines():
    p_str, v_str = txt_line[2:].split(" v=")
    px, py = map(int, p_str.split(","))
    vx, vy = map(int, v_str.split(","))
    p_final_x = (px + TIME_STEPS * vx) % WIDTH
    p_final_y = (py + TIME_STEPS * vy) % HEIGHT
    if p_final_x == WIDTH // 2 or p_final_y == HEIGHT // 2:
        continue
    quads[p_final_x > WIDTH / 2, p_final_y > HEIGHT // 2] += 1

print(np.prod(list(quads.values())))
