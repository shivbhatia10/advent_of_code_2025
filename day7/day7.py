from functools import cache

with open("input.txt") as f:
    grid: list[list[str]] = []
    for line in f:
        grid.append(list(line.strip()))

    n, m = len(grid), len(grid[0])

    @cache
    def ways(x: int, y: int) -> int:
        if x >= n:
            return 1
        if grid[x][y] == "^":
            if y == 0:
                return ways(x + 1, y + 1)
            elif y == m - 1:
                return ways(x + 1, y - 1)
            return ways(x + 1, y - 1) + ways(x + 1, y + 1)
        return ways(x + 1, y)

    start: int = [i for i, x in enumerate(grid[0]) if x == "S"][0]
    solution: int = ways(0, start)
    print(solution)

    # beam: list[bool] = [c == "S" for c in grid[0]]
    # splits: int = 0
    # n, m = len(grid), len(grid[0])
    # for x in range(1, n):
    #     for y in range(m):
    #         if beam[y] and grid[x][y] == "^":
    #             beam[y] = False
    #             if y > 0:
    #                 beam[y - 1] = True
    #             if y < m - 1:
    #                 beam[y + 1] = True
    #             splits += 1
    # print(splits)
