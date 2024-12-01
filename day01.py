import collections
from pathlib import Path

txt = (Path(__file__).parent / "inputs" / "day01.txt").read_text()

l1, l2 = zip(*map(str.split, txt.splitlines()))
print(sum(abs(int(b) - int(a)) for a, b in zip(sorted(l1), sorted(l2))))

d2 = collections.Counter(l2)
print(sum(int(a) * d2[a] for a in l1))
