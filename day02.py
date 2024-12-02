import itertools
from pathlib import Path

txt = (Path(__file__).parent / "inputs" / "day02.txt").read_text()

# generate all possible values assuming min = 0 and ignoring reversals
safe = set()
for steps in range(1, 9):  # max len; 9 is enough here
    for vals in itertools.product(*[[1, 2, 3]] * steps):
        safe.add(tuple(itertools.accumulate((0, ) + vals)))


reports = [
    [int(x) for x in line.split()]
    for line in txt.splitlines()
]
reports_normed = [
    tuple(x - min(report) for x in report)
    for report in reports
]

part1 = sum(
    report in safe or report[::-1] in safe
    for report in reports_normed
)
print(part1)

part2 = sum(
    any(
        report[:i] + report[i+1:] in safe
        for i in range(len(report) + 1)
    )
    for base_report in reports_normed
    for report in [base_report, base_report[::-1]]
)
print(part2)
