# Problem: Find Median from Data Stream - https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.first_hf = [] 
        self.second_hf = [] 

    def addNum(self, num: int) -> None:
        heapq.heappush(self.first_hf, -num)

        heapq.heappush(self.second_hf, -heapq.heappop(self.first_hf))

        if len(self.second_hf) > len(self.first_hf):
            heapq.heappush(self.first_hf, -heapq.heappop(self.second_hf))

    def findMedian(self) -> float:
        if len(self.first_hf) > len(self.second_hf):
            return -self.first_hf[0]
        return (-self.first_hf[0] + self.second_hf[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()