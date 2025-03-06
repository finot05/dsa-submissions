# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        ans = [0]*length
        stk = []
        for i in range(length):
            while stk and temperatures[i] > temperatures[stk[-1]]:
                prev_ind = stk.pop()
                ans[prev_ind] = i - prev_ind
            stk.append(i)
        return ans