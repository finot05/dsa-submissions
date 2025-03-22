# Problem: fruit-into-baskets - https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        freq = {}
        ans = 0
        for r in range(len(fruits)):
            freq[fruits[r]] = freq.get(fruits[r], 0) + 1
            while l<=r and len(freq) > 2:
                freq[fruits[l]] -= 1
                if freq[fruits[l]] == 0:
                    del freq[fruits[l]]
                    
                l += 1
            ans = max(ans, r-l+1)
        return ans