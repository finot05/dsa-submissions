# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        tree = defaultdict(list)
        for e, m in enumerate(manager):
            tree[m].append(e)
        q = deque([(headID, 0)])
        res = 0
        while q:
            emp, t = q.popleft()
            res = max(res, t)
            for e in tree[emp]:
                q.append((e,t+informTime[emp])) 
        return res