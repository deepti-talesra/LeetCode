# Video Explanation: https://www.youtube.com/watch?v=pUSy6UZCFKw&t=2s

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# preorder . root, left, right
'''
            --1
           /     \
         /         \
     --2          --3
    /     \      /     \
 --4     --5  --6     --7                  
'''
# [1,2,4,5,3,6,7]


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        stack = [root]
        result = []
        while stack != []:
            root = stack.pop()
            result.append(root.val)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)
        return result
