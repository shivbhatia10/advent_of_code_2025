import shapely
from shapely import Polygon

with open("input.txt") as f:
    points: list[tuple[float, float]] = []
    for line in f:
        line = line.strip()
        [x, y] = [float(num) for num in line.split(",")]
        points.append((x, y))
    n = len(points)

    def get_area(x1: float, y1: float, x2: float, y2: float) -> float:
        l1: float = abs(x1 - x2) + 1.0
        l2: float = abs(y1 - y2) + 1.0
        return l1 * l2

    area_full = Polygon(points)
    max_area = 0
    for i in range(n):
        (x1, y1) = points[i]
        for j in range(i + 1, n):
            (x2, y2) = points[j]

            rect = shapely.box(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
            a = get_area(x1, y1, x2, y2)
            if shapely.within(rect, area_full) and a > max_area:
                max_area = a
    print(max_area)

    # greens: set[tuple[int, int]] = set()
    # for p1, p2 in zip(points, points[1:] + [points[0]]):
    #     # Either it's a straight line horizontally or vertically
    #     x1, y1 = p1
    #     x2, y2 = p2
    #     if x1 == x2:
    #         for dy in range(abs(y2 - y1) + 1):
    #             greens.add((x1, min(y1, y2) + dy))
    #     elif y1 == y2:
    #         for dx in range(abs(x2 - x1) + 1):
    #             greens.add((min(x1, x2) + dx, y1))
    # max_x = max(x for (x, _) in points) + 2
    # max_y = max(y for (_, y) in points) + 2
    # print(max_x, max_y)

    # def is_inside(px: int, py: int) -> bool:
    #     # arbitrary I think
    #     dx, dy = 0, 1
    #     lines_crossed: int = 0
    #     while px in range(max_x) and py in range(max_y):
    #         if (px, py) in greens:
    #             lines_crossed += 1
    #         px += dx
    #         py += dy
    #     # if crossed an odd number of lines, is inside
    #     return (lines_crossed % 2) == 1

    # max_valid_area: int = 0
    # for i in range(len(points)):
    #     for j in range(i + 1, len(points)):
    #         (px1, py1) = points[i]
    #         (px2, py2) = points[j]
    #         if px1 > px2:
    #             px1, px2 = px2, px1
    #         if py1 > py2:
    #             py1, py2 = py2, py1
    #         is_valid = all(
    #             (x, y) in greens or is_inside(x, y)
    #             for x in range(px1, px2 + 1)
    #             for y in range(py1, py2 + 1)
    #         )
    #         # print(px1, py1, px2, py2, is_valid)
    #         if is_valid:
    #             max_valid_area = max(max_valid_area, (py2 - py1 + 1) * (px2 - px1 + 1))
    # print(max_valid_area)

    # dirs: list[tuple[int, int]] = [
    #     (0, 1),
    #     (0, -1),
    #     (1, 0),
    #     (-1, 0),
    # ]
    # dfs: list[tuple[int, int]] = [(0, 0)]
    # outers = {(0, 0)}
    # while dfs:
    #     # print(dfs)
    #     (cx, cy) = dfs.pop()
    #     for dx, dy in dirs:
    #         nx, ny = cx + dx, cy + dy
    #         if (
    #             nx in range(max_x)
    #             and ny in range(max_y)
    #             and (nx, ny) not in outers
    #             and (nx, ny) not in greens
    #         ):
    #             outers.add((nx, ny))
    #             dfs.append((nx, ny))

    # for y in range(max_y):
    #     for x in range(max_x):
    #         if (x, y) in greens:
    #             print("X", end="")
    #         # elif (x, y) in outers:
    #         #     print("O", end="")
    #         else:
    #             print(".", end="")
    #     print("")
