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
        ans = []
        stack = [root]
        while stack:
            temp = stack.pop()
            if temp:
                ans.append(temp.data)
                stack.append(temp.right)
                stack.append(temp.left)
        return ans
