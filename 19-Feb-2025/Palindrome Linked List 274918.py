# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        f = head
        s = head
        prev1 = s
        while f and f.next:
            prev1 = s
            s = s.next
            f = f.next.next
        prev1.next = None
        cur1 = s
        prev = None
        while cur1:
            nxt = cur1.next
            cur1.next = prev
            prev = cur1
            cur1 = nxt
        cur2 = head
        while prev and cur2:
            if prev.val != cur2.val:
                return False
            prev = prev.next
            cur2 = cur2.next
        return True 
        
