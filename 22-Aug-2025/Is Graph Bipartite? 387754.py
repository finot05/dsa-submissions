# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = {}
        for start in range(n):
            if start not in color:
                q = deque([(start, 'b')])
                while q:
                    node, c = q.popleft()
                    if node in color:
                        if color[node] != c:
                            return False
                        continue
                    color[node] = c
                    new_c = 'b' if c == 'r' else 'r'
                    for negh in graph[node]:
                        q.append((negh, new_c))
        return True