# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        output = []
        curr = [root]
        while curr:
            new_level = []
            curr_sum = 0
            for r in curr:
                if r.right:
                    new_level.append(r.right)
                if r.left:
                    new_level.append(r.left)
                curr_sum += r.val
            output.append(curr_sum/len(curr))
            curr = new_level
        return output
