# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        freq = Counter(answers)
        total_rabbits = 0

        for key, count in freq.items():
            group_size = key + 1 
            full_groups = (count + group_size - 1) // group_size 
            total_rabbits += full_groups * group_size  
            
        return total_rabbits
