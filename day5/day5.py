import heapq
from math import inf

with open("input.txt") as f:
    ranges, foods = f.read().split("\n\n")
    r = []
    for line in ranges.split("\n"):
        line = line.strip()
        [start, end] = line.split("-")
        r.append((int(start), int(end)))
    h = []
    for start, end in r:
        heapq.heappush(h, (start, 0))
        heapq.heappush(h, (end, 1))
    total = 0
    stack = 0
    start = inf
    while h:
        (curr, event_type) = heapq.heappop(h)
        print(curr, event_type)
        if event_type == 0:
            start = min(start, curr)
            stack += 1
        else:
            stack -= 1
            if stack == 0:
                total += curr + 1 - start
                start = inf
                print(total)
    print(total)
