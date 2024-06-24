# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    #Recursive Solution
    def check(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None or left.val != right.val:
            return False
        return self.check(left.left, right.right) and self.check(left.right, right.left)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.check(root.left, root.right)


    #Iterative Solution
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
            stack = [(root.left,root.right)]
            while stack:
                left, right = stack.pop()
                if left is None and right is None:
                    continue
                if left is None or right is None or left.val != right.val:
                    return False
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            return True

