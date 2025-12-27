from math import inf

with open("simple.txt") as f:
    points: list[tuple[int, int]] = []
    for line in f:
        line = line.strip()
        [x, y] = [int(num) for num in line.split(",")]
        points.append((x, y))
    n = len(points)
    greens: set[tuple[int, int]] = set()
    for p1, p2 in zip(points, points[1:] + [points[0]]):
        # Either it's a straight line horizontally or vertically
        x1, y1 = p1
        x2, y2 = p2
        if x1 == x2:
            for dy in range(abs(y2 - y1) + 1):
                greens.add((x1, min(y1, y2) + dy))
        elif y1 == y2:
            for dx in range(abs(x2 - x1) + 1):
                greens.add((min(x1, x2) + dx, y1))
    max_x = max(x for (x, _) in points) + 2
    max_y = max(y for (_, y) in points) + 2
    print(max_x, max_y)

    dirs: list[tuple[int, int]] = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]
    dfs: list[tuple[int, int]] = [(0, 0)]
    outers = {(0, 0)}
    while dfs:
        # print(dfs)
        (cx, cy) = dfs.pop()
        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            if (
                nx in range(max_x)
                and ny in range(max_y)
                and (nx, ny) not in outers
                and (nx, ny) not in greens
            ):
                outers.add((nx, ny))
                dfs.append((nx, ny))

    for x in range(max_x):
        for y in range(max_y):
            if (x, y) in greens:
                print("X", end="")
            elif (x, y) in outers:
                print("O", end="")
            else:
                print(".", end="")
        print("")
