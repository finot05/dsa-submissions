# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.array = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.array.append(node.val)
            inorder(node.right)
        def recurse(arr):
            if not arr:
                return None
            mid = len(arr)//2
            mid_val = arr[mid]
            
            node = TreeNode(mid_val)
            node.left = recurse(arr[:mid])
            node.right = recurse(arr[mid+1:])
            
            return node
        inorder(root)
        return recurse(self.array)