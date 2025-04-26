# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        columns = defaultdict(list)
        min_ind, max_ind = float('inf'), float('-inf')
        queue = deque([(root, 0)]) #node, col_ind
        while queue:
            node, col_ind = queue.popleft()
            min_ind = min(min_ind, col_ind)
            max_ind = max(max_ind, col_ind)
            columns[col_ind].append(node.val)
            if node.left:
                queue.append((node.left, col_ind-1))
            if node.right:
                queue.append((node.right, col_ind+1))
        output = []
        for col in range(min_ind, max_ind+1):
            output.append(columns[col])
        return output
