from math import inf


def get_joltage(digits: list[int], rem: int) -> int:
    if rem == 1:
        return max(digits)
    curr = -inf
    index = -1
    for i, x in enumerate(digits[: -(rem - 1)]):
        if x > curr:
            curr = x
            index = i
    return curr * (10 ** (rem - 1)) + get_joltage(digits[index + 1 :], rem - 1)


with open("input.txt") as f:
    joltage = 0
    for line in f:
        line = line.strip()
        digits = [int(c) for c in line]
        joltage += get_joltage(digits, 12)

    print(joltage)
