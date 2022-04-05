# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int: 
        max_width = 1
        curr_level = [(root, 1)] #root, pos
        while curr_level != []:
            next_level = []
            for roots, pos in curr_level:
                if roots.left:
                    next_level.append((roots.left, pos*2))
                if roots.right:
                    next_level.append((roots.right, pos*2+1))
            if next_level != []:
                max_width = max(max_width, next_level[-1][1]-next_level[0][1]+1)
            curr_level = next_level
        return max_width
