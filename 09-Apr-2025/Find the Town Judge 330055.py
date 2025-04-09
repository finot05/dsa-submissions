# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        t_count = defaultdict(int)   
        t_by_count = defaultdict(int)  

        for a, b in trust:
            t_count[a] += 1
            t_by_count[b] += 1

        for i in range(1, n + 1):
            if t_count[i] == 0 and t_by_count[i] == n - 1:
                return i

        return -1