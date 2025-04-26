# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]
        indegree = [0]*n
        for a, b in richer:
            graph[a].append(b)
            indegree[b] += 1
        
        que = deque()
        for i in range(n):
            if indegree[i] == 0:
                que.append(i)
        
        ans = [i for i in range(n)]

        while que:
            src = que.popleft()
            for nei in graph[src]:
                if quiet[src] < quiet[nei]:
                    quiet[nei] = quiet[src]
                    ans[nei] = ans[src]
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    que.append(nei)
        
        return ans