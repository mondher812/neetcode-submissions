# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q:
            return False
        if q is None and p:
            return False
        if p and q and p.val == q.val:
            if self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left):
                return True
            return False
        if p is None and q is None:
            return True
        return False