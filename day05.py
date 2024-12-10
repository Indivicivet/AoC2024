from collections import defaultdict

from aocd import data

raw_page_rules, raw_updates = data.split("\n\n")

page_order_graph = defaultdict(list)
for row in raw_page_rules.splitlines():
    pg1, pg2 = row.split("|")
    page_order_graph[pg1].append(pg2)
updates = [row.split(",") for row in raw_updates.splitlines()]
result = sum(
    int(update[len(update) // 2])
    for update in updates
    if all(
        later_page not in update[:i]
        for i, v in enumerate(update)
        for later_page in page_order_graph[v]
    )
)
print(result)
