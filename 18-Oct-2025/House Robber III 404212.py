# Problem: House Robber III - https://leetcode.com/problems/house-robber-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [0, 0]
            
            l = dfs(node.left)
            r = dfs(node.right)

            rob_this = node.val + l[1] + r[1]
            skip_this = max(l) + max(r)

            return [rob_this, skip_this]
        
        return max(dfs(root))