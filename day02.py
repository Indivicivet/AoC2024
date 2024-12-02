import itertools
from pathlib import Path

txt = (Path(__file__).parent / "inputs" / "day02.txt").read_text()

reports = [
    [int(x) for x in line.split()]
    for line in txt.splitlines()
]

# generate all possible values assuming min = 0 and ignoring reversals
safe = set()
for steps in range(1, 9):  # max len; 9 is enough here
    for vals in itertools.product(*[[1, 2, 3]] * steps):
        safe.add(tuple(itertools.accumulate((0, ) + vals)))


def is_safe(r):
    return tuple(x - min(r) for x in r) in safe


part1 = sum(
    is_safe(report) or is_safe(report[::-1])
    for report in reports
)
print(part1)

part2 = sum(
    any(
        is_safe(report[:i] + report[i+1:])
        for report in [base_report, base_report[::-1]]
        for i in range(len(report))
    )
    for base_report in reports
)
print(part2)
