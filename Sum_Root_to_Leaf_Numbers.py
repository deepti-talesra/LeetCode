# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        
        def dfs(r, curr):
            curr = (curr * 10) + r.val
            if r.left is None and r.right is None:
                self.total += curr
            if r.left:
                dfs(r.left, curr)
            if r.right:
                dfs(r.right, curr)
        
        dfs(root, 0)
        return self.total
