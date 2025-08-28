# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        q = deque([i for i in range(n) if indegree[i] == 0])
        ancestors = [set() for _ in range(n)]

        while q:
            u = q.popleft()
            for v in graph[u]:
                ancestors[v].add(u)
                ancestors[v].update(ancestors[u])
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        return [sorted(list(s)) for s in ancestors]