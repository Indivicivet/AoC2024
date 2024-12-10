from collections import defaultdict
import random

from tqdm import tqdm

from aocd import data

raw_page_rules, raw_updates = data.split("\n\n")

page_order_graph = defaultdict(list)
for row in raw_page_rules.splitlines():
    pg1, pg2 = row.split("|")
    page_order_graph[pg1].append(pg2)
updates = [row.split(",") for row in raw_updates.splitlines()]


def is_ok(upd):
    return all(
        later_page not in upd[:i]
        for i, v in enumerate(upd)
        for later_page in page_order_graph[v]
    )


result = sum(
    int(update[len(update) // 2])
    for update in updates
    if is_ok(update)
)
print(result)

result_all_fixed = 0
for update in tqdm(updates):
    while not is_ok(update):
        random.shuffle(update)  # this is insanely slow.
    result_all_fixed += int(update[len(update) // 2])
print(result_all_fixed - result)
