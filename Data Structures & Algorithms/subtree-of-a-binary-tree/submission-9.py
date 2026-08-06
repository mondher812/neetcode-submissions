# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p is None and q:
                return False
            if q is None and p:
                return False
            if p and q and p.val == q.val:
                if isSameTree(p.right,q.right) and isSameTree(p.left,q.left):
                    return True
                return False
            if p is None and q is None:
                return True
            return False  
        if not root and not subRoot:
            print("here1")
            return True
        if not root:
            print("here2")

            return False
        if not subRoot:
            print("here3")
            return False
        if root.val == subRoot.val:
            if isSameTree(root,subRoot):
                return True

            
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
            