# 743. Network Delay Time
# https://leetcode.com/problems/network-delay-time/description/
from typing import List
from collections import defaultdict

# WIP
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        node_time_map = defaultdict(dict)

        for time in times:
            node_time_map[time[0]][time[1]] = time[2]

        min_times = {i: float('inf') for i in range(1, n+1)}
        min_times[k] = 0
        visited = set()
        stack = [k]
        while len(stack) > 0:
            target = stack.pop()
            visited.add(target)
            for key, value in node_time_map[target].items():
                min_times[key] = min(min_times[key], min_times[target] + value)
                if key not in visited:
                    stack.append(key)

        if len(visited) == n:
            return max(min_times.values())
        return -1


def quick_sort(input):
    if len(input) <= 1:
        return input

    low = []
    high = []
    pivot = input[0]

    for x in input[1:]:
        if x < pivot:
            low.append(x)
        else:
            high.append(x)

    return quick_sort(low) + [pivot] + quick_sort(high)
