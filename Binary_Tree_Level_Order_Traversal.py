# Video Explanation: https://www.youtube.com/watch?v=MBZ-gBkjdMc

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''           1
           /     \
         /         \
       2            3
    /     \      /     \
   4       5    6       7     
'''
# queue = []; next_queue = []; level = []; result = [[1], [2,3],[4,5,6,7]]
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        next_queue = []
        level = []
        result = []
        while queue != []:
            for root in queue:
                level.append(root.val)
                if root.left is not None:
                    next_queue.append(root.left)
                if root.right is not None:
                    next_queue.append(root.right)
            result.append(level)
            level = []
            queue = next_queue
            next_queue = []
        return result
