# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Iterative
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        result = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

      # Recursive
      def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.result = None
        
        def inOrder(root):
            if root is None or self.result is not None:
                return
            inOrder(root.left)
            self.k -= 1
            if self.k == 0:
                self.result = root.val
                return
            inOrder(root.right)
            
        inOrder(root)
        return self.result
