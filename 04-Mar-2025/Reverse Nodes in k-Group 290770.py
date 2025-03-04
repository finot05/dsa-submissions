# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy  
        while True:
            kth = prev_group_tail
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  

            prev, curr = kth.next, prev_group_tail.next
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            temp = prev_group_tail.next
            prev_group_tail.next = prev
            prev_group_tail = temp
        