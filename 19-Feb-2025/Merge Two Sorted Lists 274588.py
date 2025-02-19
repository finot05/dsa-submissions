# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        else:
            f = list1
            s = list2
            dummy = ListNode()
            curr = dummy
            while f and s:
                if f.val < s.val:
                    curr.next = f
                    f = f.next

                else:
                    curr.next = s
                    s = s.next
                curr = curr.next

            if f:
                curr.next = f
            elif s:
                curr.next = s

        return dummy.next