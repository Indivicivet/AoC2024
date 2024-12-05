"""
not figured out how it works yet, but might be able to extract
XMAS matches from fourier transform data?

taking exp(phase of array), you could convolve with exp(phase 0, 1, 2, 3)
in various directions and extract all matches as things with magnitude 4;
can you do that nicely using an FFT to get all matches at once?
"""

from aocd import data
import numpy as np
from scipy import signal
from PIL import Image

arr = np.array([
    ["XMAS".index(v) for v in row]
    for row in data.splitlines()
])
print(arr)

PHASE_RATE = np.pi / 4
phased = np.exp(1j * PHASE_RATE * arr)
template_raw = np.exp(-1j * PHASE_RATE * np.arange(4)[:, np.newaxis])

convs = [
    signal.convolve(phased, template[::traverse_sign, ::traverse_sign])
    for template in [
        template_raw,
        template_raw.T,  # vertical
        np.diagflat(template_raw),  # diagonal
        np.flipud(np.diagflat(template_raw)),  # the other diagonal...
    ]
    for traverse_sign in [-1, 1]
]
print(sum(
    np.sum(np.abs(conv) > 4 - 0.001)
    for conv in convs
))

# fourier = np.fft.fft2(phased)
# Image.fromarray(10 * np.abs(fourier) ** 0.5).show()

phased_pt2 = phased * (arr > 0)  # remove X's
assert PHASE_RATE == np.pi / 2, "using hardcoded phase values for part 2 :)"
template_pt2_raw = np.array([[1, 0, 1], [0, 1j, 0], [-1, 0, -1]])
convs_pt2 = [
    signal.convolve(phased_pt2, template[::traverse_ud, :])
    for template in [template_pt2_raw, template_pt2_raw.T]
    for traverse_ud in [-1, 1]
]
print(sum(
    np.sum(np.abs(conv) > 5 - 0.01)
    for conv in convs_pt2
))
