from collections import defaultdict
from functools import cache

with open("input.txt") as f:
    adj: dict[str, list[str]] = defaultdict(list)
    for line in f:
        line = line.strip()
        pieces: list[str] = line.split(" ")
        adj[pieces[0][:-1]] = pieces[1:][:]

    @cache
    def ways(start: str, seen_dac: bool, seen_fft: bool) -> int:
        if start == "out":
            if seen_dac and seen_fft:
                return 1
            return 0
        return sum(
            ways(nei, seen_dac or (start == "dac"), seen_fft or (start == "fft"))
            for nei in adj[start]
        )

    print(ways("svr", False, False))

    # ways: int = 0
    # dfs: list[str] = ["you"]
    # while dfs:
    #     curr = dfs.pop()
    #     if curr == "out":
    #         ways += 1
    #     for nei in adj[curr]:
    #         dfs.append(nei)
    # print(ways)

    # def num_ways(start: str, end: str, ignoring: set[str]) -> int:
    #     dfs: list[tuple[str, int]] = [(start, 0)]
    #     ways: int = 0
    #     while dfs:
    #         curr, curr_dist = dfs.pop()
    #         print(curr, curr_dist)
    #         if curr in ignoring or curr_dist > 700:
    #             continue
    #         if curr == end:
    #             ways += 1
    #         for nei in adj[curr]:
    #             dfs.append((nei, curr_dist + 1))
    #     return ways

    # svr_to_dac: int = num_ways("svr", "dac", {"fft", "out"})
    # print(svr_to_dac)
    # dac_to_fft: int = num_ways("dac", "fft", {"svr", "out"})
    # print(dac_to_fft)
    # fft_to_out: int = num_ways("fft", "out", {"svr", "dac"})
    # print(fft_to_out)
    # ways1: int = svr_to_dac * dac_to_fft * fft_to_out

    # svr_to_fft: int = num_ways("svr", "fft", {"dac", "out"})
    # print(svr_to_fft)
    # fft_to_dac: int = num_ways("fft", "dac", {"svr", "out"})
    # print(fft_to_dac)
    # dac_to_out: int = num_ways("dac", "out", {"svr", "fft"})
    # print(dac_to_out)
    # ways2: int = svr_to_fft * fft_to_dac * dac_to_out

    # print(ways1 + ways2)
