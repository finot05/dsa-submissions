# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        self.max_tot = float('inf')
        self.children = [0] * k
        def backtrack(idx):
            if idx >= n:
                self.max_tot = min(self.max_tot, max(self.children))
                return
            for i in range(k):
                self.children[i] += cookies[idx]
                backtrack(idx+1)
                self.children[i] -= cookies[idx]
                if self.children[i] == 0:
                    break
        backtrack(0)
        return self.max_tot