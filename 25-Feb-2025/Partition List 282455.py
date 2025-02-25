# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lh, mh = ListNode(), ListNode()
        lc, mc = lh, mh
        cur = head
        while cur:
            if cur.val >= x:
                mc.next = cur
                mc = mc.next
            else:
                lc.next = cur
                lc = lc.next
            cur = cur.next
        lc.next = mh.next
        mc.next = None
        return lh.next        