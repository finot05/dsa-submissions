# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        first_half = []
        res = 0
        n = 0
        cur = head
        while cur:
            cur = cur.next
            n += 1

        for _ in range(n//2):
            first_half.append(head.val)
            head = head.next

        while head:
            twin = first_half.pop()
            res = max(res, (twin + head.val))
            head = head.next

        return res