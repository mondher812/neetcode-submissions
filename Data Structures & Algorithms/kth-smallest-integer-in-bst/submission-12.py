# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = 0
        self.ret = root.val
        def traverse(node):
            if node is None:
                return 
                 
            traverse(node.left)  
            self.cnt+=1
            if self.cnt == k:
                self.ret = node.val
            traverse(node.right)

        traverse(root)
        return self.ret
            
        