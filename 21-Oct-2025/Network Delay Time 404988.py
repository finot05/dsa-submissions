# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        heap = [(0, k)]
        visited = set()
        t = 0
        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in visited:
                continue
            visited.add(n1)
            t = max(t, w1)
            for n2, w2 in adj[n1]:
                heapq.heappush(heap, (w2+w1, n2))

        return t if len(visited) == n else -1