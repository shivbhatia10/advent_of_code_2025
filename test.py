from collections import defaultdict, deque


# Unit conversion
class UnitConverter:
    def __init__(self):
        self.adj: dict[str, list[tuple[float, str]]] = defaultdict(list)

    def parse_fact(self, origin: str, factor: float, target: str):
        if factor == 0:
            raise Exception("Found conversion factor of 0")
        self.adj[origin].append((factor, target))
        self.adj[target].append((1 / factor, origin))

    def answer_query(self, init_value: float, origin: str, target: str) -> float:
        bfs: list[tuple[float, str]] = deque([(init_value, origin)])
        visited: set[str] = {origin}
        while bfs:
            value, unit = bfs.popleft()
            if unit == target:
                return value
            for factor, converted_unit in self.adj[unit]:
                if converted_unit not in visited:
                    visited.add(converted_unit)
                    bfs.append((value * factor, converted_unit))
        raise Exception("Could not convert origin unit into target unit")
