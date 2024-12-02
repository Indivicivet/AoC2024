from collections import defaultdict
import itertools
from pathlib import Path

txt = (Path(__file__).parent / "inputs" / "day02.txt").read_text()

# generate all possible values assuming min = 0 and ignoring reversals
safe_by_len = defaultdict(set)
for steps in range(1, 9):  # max len; 9 is enough here
    for vals in itertools.product(*[[1, 2, 3]] * steps):
        safe_by_len[steps + 1].add(tuple(itertools.accumulate((0, ) + vals)))

reports = [
    [int(x) for x in line.split()]
    for line in txt.splitlines()
]
reports_normed = [
    tuple(x - min(report) for x in report)
    for report in reports
]

part1 = sum(
    report in safe_by_len[len(report)] or report[::-1] in safe_by_len[len(report)]
    for report in reports_normed
)
print(part1)
