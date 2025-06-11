# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(list)

        # Build bidirectional weighted graph
        for (a, b), val in zip(equations, values):
            graph[a].append((b, val))
            graph[b].append((a, 1 / val))

        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0

            visited = set()
            que = deque([(start, 1.0)])

            while que:
                node, val = que.popleft()
                if node == end:
                    return val
                visited.add(node)
                for nei, weight in graph[node]:
                    if nei not in visited:
                        que.append((nei, val * weight))
            return -1.0

        result = []
        for x, y in queries:
            result.append(bfs(x, y))

        return result