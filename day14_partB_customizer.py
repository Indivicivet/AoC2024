import itertools

from aocd import data  # used for velocity
import numpy as np
from PIL import Image

WIDTH = 101
HEIGHT = 103


def from_image_path(path, iter_n_times=1234):
    image_data = np.array(Image.open(path).convert("L"))
    print("custom image! number of robots:", (image_data > 0).sum())
    assert image_data.shape == (HEIGHT, WIDTH), (
        f"{image_data.shape} != {(HEIGHT, WIDTH)}"
    )
    txt_line_iter = itertools.cycle(data.splitlines())
    data_out_list = []
    for j in range(image_data.shape[0]):
        for i in range(image_data.shape[1]):
            if image_data[j, i]:
                # ignore position
                _, v_str = next(txt_line_iter).split(" v=")
                vx, vy = map(int, v_str.split(","))
                px = (i - vx * iter_n_times) % WIDTH
                py = (j - vy * iter_n_times) % HEIGHT
                data_out_list.append(f"p={px},{py} v={vx},{vy}")
    return "\n".join(data_out_list)


if __name__ == "__main__":
    print(from_image_path("extras/xmas_tree_1.png"))
