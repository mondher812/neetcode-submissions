# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = []
        out = []
        q.append(root)
        while len(q)>0:
            level = []
            r = len(q)
            for i in range(r):
                popped = q.pop(0)
                if popped:
                    q.append(popped.left)
                    q.append(popped.right)
                    level.append(popped.val)
            if len(level) > 0:
                out.append(level)
        return out


       