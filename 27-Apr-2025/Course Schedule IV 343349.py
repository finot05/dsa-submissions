# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            graph[u].append(v)
        reached = {}
        def dfs(u):
            if u in reached:
                return reached[u]
            visited = set()
            for v in graph[u]:
                visited.add(v)
                visited.update(dfs(v))
            reached[u] = visited
            return visited

        for i in range(numCourses):
            dfs(i)
        
        ans = []
        for u, v in queries:
            ans.append(v in reached[u])

        return ans