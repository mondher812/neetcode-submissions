# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.dif = 0
        def height(node):
            if node is None:
                return 0
            lh = height(node.left)
            rh = height(node.right)
            self.dif = max(self.dif,(max(lh,rh) - min(lh,rh)))
            return 1 + max(height(node.left),height(node.right))
        height(root)
        if self.dif > 1:
            return False
        return True

        
        