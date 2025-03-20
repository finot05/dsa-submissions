# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.total = 0
        def convertBST(node):
            if not node:
                return
            convertBST(node.right)

            self.total += node.val
            node.val = self.total

            convertBST(node.left)
        convertBST(root)
        return root