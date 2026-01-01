from pulp import (
    PULP_CBC_CMD,
    LpInteger,
    LpMinimize,
    LpProblem,
    LpStatus,
    LpVariable,
    lpSum,
)

# from collections import deque

# def min_presses(line: str) -> int:
#     parts = line.split(" ")
#     source_string = parts[0][1:-1]
#     source = 0
#     for i, c in enumerate(source_string):
#         if c == "#":
#             source |= 1 << i
#     button_strings: list[str] = parts[1:-1]
#     buttons: list[int] = []
#     for bs in button_strings:
#         bs = bs[1:-1]
#         x = 0
#         for d in bs.split(","):
#             d = int(d)
#             x |= 1 << d
#         buttons.append(x)
#     bfs = deque([(source, 0)])
#     visited: set[int] = {source}
#     while bfs:
#         curr, curr_dist = bfs.popleft()
#         if curr == 0:
#             return curr_dist
#         for button in buttons:
#             next = curr ^ button
#             if next not in visited:
#                 bfs.append((next, curr_dist + 1))
#                 visited.add(next)
#     raise Exception("Not found")


def min_joults(line: str) -> int:
    parts = line.split(" ")
    source_string = parts[-1][1:-1]
    source: list[int] = []
    for c in source_string.split(","):
        source.append(int(c))
    button_strings: list[str] = parts[1:-1]
    buttons: list[list[int]] = []
    for bs in button_strings:
        bs = bs[1:-1]
        buttons.append([int(c) for c in bs.split(",")])

    res = pulp_solver(source, buttons)
    return res


def pulp_solver(target: list[int], buttons: list[list[int]]) -> int:
    # target: list of ints, buttons: list of lists of ints (which indices each button increments)
    n = len(target)
    prob = LpProblem("buttons", LpMinimize)

    # one variable per button: how many times we press it
    x = [LpVariable(f"b{i}", lowBound=0, cat=LpInteger) for i in range(len(buttons))]

    # minimize total presses
    prob += lpSum(x)

    # constraints: each position must hit its target
    for pos in range(n):
        contrib = lpSum(x[i] for i, btn in enumerate(buttons) if pos in btn)
        prob += contrib == target[pos]

    prob.solve(PULP_CBC_CMD(msg=False))

    if LpStatus[prob.status] == "Optimal":
        return int(sum(v.varValue for v in x))
    return None  # no solution


def apply_button(curr: int, button: int, n: int) -> int | None:
    res = 0
    for i in range(n):
        chunk: int = (curr >> (9 * i)) & (2**9 - 1)
        chunk -= (button >> i) & 1
        if chunk < 0:
            return None
        res |= chunk << (9 * i)
    return res


with open("simple.txt") as f:
    s: int = 0
    for line in f:
        line = line.strip()
        # print(line)
        m = min_joults(line)
        s += m
        print(line, m)
    print(s)
