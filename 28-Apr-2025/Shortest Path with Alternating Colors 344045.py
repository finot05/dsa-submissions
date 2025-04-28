# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        dr_graph = defaultdict(list)
        for a, b in redEdges:
            dr_graph[a].append((b, 0))
        for u, v in blueEdges:
            dr_graph[u].append((v, 1))
        
        visited = [[0,0] for _ in range(n)]
        visited[0][0] = 1
        visited[0][1] = 1
        que = deque([[0, 0], [0, 1]])
        count = 0
        ans = [-1]*n
        while que:
            for _ in range(len(que)):
                node, pre_color = que.popleft()
                ans[node] = count if ans[node] == -1 else ans[node]
                for nei, cur_color in dr_graph[node]:
                    if pre_color != cur_color and not visited[nei][cur_color]:
                        visited[nei][cur_color] = 1
                        que.append([nei, cur_color])
            count +=1
        return ans