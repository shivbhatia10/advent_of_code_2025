from functools import cache


@cache
def is_invalid(x: int) -> bool:
    s: str = str(x)
    n = len(s)
    for i in range(1, n):
        slice = s[:i]
        repeated = slice * (n // i)
        if repeated == s:
            print(x)
            return True
    return False


with open("input.txt") as f:
    ranges = [pair.split("-") for pair in f.read().split(",")]
    ranges = [(int(s), int(e)) for [s, e] in ranges]
    print(ranges)
    invalids: int = 0
    for s, e in ranges:
        invalids += sum(x if is_invalid(x) else 0 for x in range(s, e + 1))
    print(invalids)
