from collections import defaultdict

from aocd import data

raw_page_rules, raw_updates = data.split("\n\n")

page_order_graph = defaultdict(list)
for row in raw_page_rules.splitlines():
    pg1, pg2 = row.split("|")
    page_order_graph[pg1].append(pg2)
updates = [row.split(",") for row in raw_updates.splitlines()]


def find_first_violation_indices(upd):
    try:
        return next(
            (i, upd.index(later_page))
            for i, v in enumerate(upd)
            for later_page in page_order_graph[v]
            if later_page in upd[:i]
        )
    except StopIteration:
        return None


result = sum(
    int(update[len(update) // 2])
    for update in updates
    if find_first_violation_indices(update) is None
)
print(result)

result_all_fixed = 0
for update in updates:
    while (ab := find_first_violation_indices(update)) is not None:
        # if we have any mismatches, swap them, until we're sorted
        update[ab[0]], update[ab[1]] = update[ab[1]], update[ab[0]]
    result_all_fixed += int(update[len(update) // 2])
print(result_all_fixed - result)
