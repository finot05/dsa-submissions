# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return float("inf")
            if rem in memo:
                return memo[rem]
            best = float("inf")
            for c in coins:
                best = min(best, 1 + dp(rem - c))
            memo[rem] = best
            return best

        ans = dp(amount)
        return ans if ans != float("inf") else -1

            
            