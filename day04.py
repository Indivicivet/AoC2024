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
    ]
    for traverse_sign in [-1, 1]
]
print(sum(
    np.sum(np.abs(conv > 4 - 0.001))
    for conv in convs
))

# fourier = np.fft.fft2(phased)
# Image.fromarray(10 * np.abs(fourier) ** 0.5).show()
