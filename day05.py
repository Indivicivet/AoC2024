from aocd import data

raw_page_rules, raw_updates = data.split("\n\n")

page_order_graph = dict(row.split("|") for row in raw_page_rules.splitlines())
updates = [row.split(",") for row in raw_updates.splitlines()]
result = 0
for update in updates:
    update_ok = True
    for i, v in enumerate(update):
        if page_order_graph[v] in update[:i]:
            update_ok = False
    if update_ok:
        result += int(update[len(update) // 2])
print(result)
