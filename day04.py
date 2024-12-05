"""
not figured out how it works yet, but might be able to extract
XMAS matches from fourier transform data?

taking exp(phase of array), you could convolve with exp(phase 0, 1, 2, 3)
in various directions and extract all matches as things with magnitude 4;
can you do that nicely using an FFT to get all matches at once?
"""

from aocd import data
import numpy as np
from PIL import Image

arr = np.array([
    ["XMAS".index(v) for v in row]
    for row in data.splitlines()
])
print(arr)

phased = np.exp(1j * 0.1 * arr)

# fourier = np.fft.fft2(phased)
# Image.fromarray(10 * np.abs(fourier) ** 0.5).show()
