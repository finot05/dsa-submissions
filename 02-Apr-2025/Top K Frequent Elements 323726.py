# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = Counter(nums)
        buckets = [[] for i in range(n+1)]
        ans = []
        for num in freq:
            buckets[freq[num]].append(num)
        for i in range(n, 0, -1):
            if buckets[i]:
                ans.extend(buckets[i])
            if len(ans) >= k:
                break

        return ans[:k+1]