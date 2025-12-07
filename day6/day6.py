from math import prod

with open("input.txt") as f:
    lines: list[str] = []
    for line in f:
        lines.append("".join(c for c in line if c != "\n"))

    # point to operator line
    i = 0
    curr_op: str | None = None
    curr_nums: list[int] = []
    total = 0
    while i < len(lines[-1]):
        if lines[-1][i] != " ":
            curr_op = lines[-1][i]
        if all(lines[c][i] == " " for c in range(len(lines))):
            if curr_op == "+":
                total += sum(curr_nums)
            else:
                total += prod(curr_nums)
            curr_nums = []
        s = "".join(lines[x][i] for x in range(len(lines) - 1))
        s = s.strip()
        if len(s) > 0:
            curr_nums.append(int(s))
        i += 1
    if curr_op == "+":
        total += sum(curr_nums)
    else:
        total += prod(curr_nums)

    print(total)
