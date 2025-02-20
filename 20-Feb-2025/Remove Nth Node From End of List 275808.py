# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = ListNode()
        d.next = head
        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        print
        count2 = 0
        curr = d
        while count2 < count - n:
            curr = curr.next
            count2 += 1
        
        curr.next = curr.next.next
        return d.next