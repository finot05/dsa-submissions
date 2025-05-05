# Problem: Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        count = 0
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, count, l))
                count += 1
        
        dummy = ListNode(0)
        curr = dummy
        
        while heap:
            val, c, smallest = heapq.heappop(heap)
            curr.next = smallest
            curr = curr.next
            if smallest.next:
                count += 1
                heapq.heappush(heap, (smallest.next.val, count, smallest.next))

        
        return dummy.next