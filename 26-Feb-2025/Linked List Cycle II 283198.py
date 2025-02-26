# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return

        l, r = head, head
        while r and r.next:
            l = l.next
            r = r.next.next

            if l == r:
               l = head
               break

        if l != head:
            return

        while l != r:
            l = l.next
            r = r.next

        return l                