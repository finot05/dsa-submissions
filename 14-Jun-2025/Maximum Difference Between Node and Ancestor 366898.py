# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, min_, max_):
            if not node:
                return max_ - min_
            min_ = min(node.val, min_)
            max_ = max(node.val, max_)

            left = dfs(node.left, min_, max_)
            right = dfs(node.right, min_, max_)
            return max(left, right)
        return dfs(root, root.val, root.val)
