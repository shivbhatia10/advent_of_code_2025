import heapq
from collections import defaultdict


class UnionFind:
    def __init__(self, points: list[tuple[int, int, int]]) -> None:
        self.points = points
        self.parents: dict[tuple[int, int, int], tuple[int, int, int]] = {
            point: point for point in self.points
        }
        self.ranks: dict[tuple[int, int, int], int] = {
            point: 0 for point in self.points
        }

    def find(self, point: tuple[int, int, int]) -> tuple[int, int, int]:
        if self.parents[point] == point:
            return point
        return self.find(self.parents[point])

    def union(self, a: tuple[int, int, int], b: tuple[int, int, int]) -> bool:
        root_a: tuple[int, int, int] = self.find(a)
        root_b: tuple[int, int, int] = self.find(b)
        if root_a == root_b:
            return False

        if self.ranks[root_a] > self.ranks[root_b]:
            self.parents[root_b] = root_a
        elif self.ranks[root_a] < self.ranks[root_b]:
            self.parents[root_a] = root_b
        else:
            self.parents[root_b] = root_a
            self.ranks[root_a] += 1
        return True

    def get_parents_to_points(
        self,
    ) -> dict[tuple[int, int, int], list[tuple[int, int, int]]]:
        parent_to_points: dict[tuple[int, int, int], list[tuple[int, int, int]]] = (
            defaultdict(list)
        )
        for point in points:
            parent_to_points[uf.find(point)].append(point)
        return parent_to_points


with open("input.txt") as f:
    points: list[tuple[int, int, int]] = []
    for line in f:
        line = line.strip()
        point: tuple[int, int, int] = tuple([int(x) for x in line.split(",")])
        points.append(point)

    n = len(points)
    h: list[tuple[int, tuple[tuple[int, int, int], tuple[int, int, int]]]] = []
    for x in range(n):
        for y in range(x + 1, n):
            (x1, y1, z1) = points[x]
            (x2, y2, z2) = points[y]
            dist: int = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
            h.append((dist, points[x], points[y]))
    heapq.heapify(h)
    uf: UnionFind = UnionFind(points)
    while h:
        d, p1, p2 = heapq.heappop(h)
        uf.union(p1, p2)
        parent_to_points = uf.get_parents_to_points()
        if len(parent_to_points.keys()) == 1:
            print(p1[0] * p2[0])
            break
    # pairs_formed: int = 0
    # while h and pairs_formed < 1000:
    #     d, p1, p2 = heapq.heappop(h)
    #     uf.union(p1, p2)
    #     pairs_formed += 1

    # parent_to_points = uf.get_parents_to_points()
    # circuit_sizes: list[int] = [len(points) for points in parent_to_points.values()]
    # circuit_sizes.sort(reverse=True)
    # print(circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2])
