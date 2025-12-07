dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

with open("input.txt") as f:
    grid: list[list[str]] = []
    for line in f:
        grid.append(list(line.strip()))
    n, m = len(grid), len(grid[0])
    reachable = 0
    done = False
    while not done:
        done = True
        for x in range(n):
            for y in range(m):
                if grid[x][y] == ".":
                    continue
                papers = 0
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if nx in range(n) and ny in range(m) and grid[nx][ny] == "@":
                        papers += 1
                if papers < 4:
                    reachable += 1
                    grid[x][y] = "."
                    done = False
    print(reachable)
