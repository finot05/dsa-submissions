# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if maxDoubles == 0 or target == 1:
            return target-1
        num = target
        c = 0
        while num > 1:
            if num % 2 ==0 and maxDoubles :
                c += 1
                maxDoubles -= 1
                num //= 2
            else:
                c += 1
                num -= 1
            
            if maxDoubles == 0:
                break
        
        c += (num - 1)

        return c 