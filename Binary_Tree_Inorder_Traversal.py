# Video Explanation: https://www.youtube.com/watch?v=RJhh3Jcc9zw

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# inorder: left, root, right
'''           1
           /  |  \
         /         \
       2            3
    /  |  \      /  |  \
   4       5    6       7
   |       |    |       |      
'''
# [4,2,5,1,6,3,7]


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        result = []
        while root is not None or stack != []:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result
