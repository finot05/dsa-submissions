# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indeg = [0 for _ in range(numCourses)]
        que = deque()
        ans = []
        for c, pre in prerequisites:
            graph[pre].append(c)
            indeg[c] += 1
        for i in range(numCourses):
            if indeg[i] == 0:
                que.append(i)
        while que:
            src = que.popleft()
            ans.append(src)
            for nei in graph[src]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    que.append(nei)
        
        if len(ans) != numCourses:
            return []
        return ans
            
