# Problem: Convert Sorted Array to Binary Search Tree - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # self.node = None
        def recurse(arr):
            if not arr:
                return None
            mid = len(arr)//2
            mid_val = arr[mid]
            
            node = TreeNode(mid_val)
            node.left = recurse(arr[:mid])
            node.right = recurse(arr[mid+1:])
            
            return node
        return recurse(nums)
        