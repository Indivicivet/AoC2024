import collections

from aocd import data

l1, l2 = zip(*map(str.split, data.splitlines()))
print(sum(abs(int(b) - int(a)) for a, b in zip(sorted(l1), sorted(l2))))

d2 = collections.Counter(l2)
print(sum(int(a) * d2[a] for a in l1))
