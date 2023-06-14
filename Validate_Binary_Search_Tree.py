# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, root, left, right):
        if root is None:
            return True
        if not (left < root.val < right):
            return False
        return self.helper(root.left, left, root.val) and self.helper(root.right, root.val, right)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float('-inf'), float('inf'))
    
