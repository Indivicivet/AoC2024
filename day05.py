from aocd import data

raw_page_rules, raw_updates = data.split("\n\n")

page_order_graph = dict(row.split("|") for row in raw_page_rules.splitlines())
updates = [row.split(",") for row in raw_updates.splitlines()]
result = sum(
    int(update[len(update) // 2])
    for update in updates
    if all(page_order_graph[v] not in update[:i] for i, v in enumerate(update))
)
print(result)
