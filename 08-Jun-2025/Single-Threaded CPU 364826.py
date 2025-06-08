# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for idx,task in enumerate(tasks):
            task.append(idx)
        order=[]
        tasks.sort()
        heap=[]
        idx=0
        time=tasks[0][0]
        while heap or idx<len(tasks):
            while idx <len(tasks) and time >=tasks[idx][0]:
                heappush(heap,[tasks[idx][1],tasks[idx][2]])
                idx+=1
            if not heap:
                time=tasks[idx][0]
            else:

                pt,index=heappop(heap)
                order.append(index)
                time+=pt
        return order