# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        qu = collections.deque()

        out= []
        qu.append(root)
        while len(qu)>0:
            r = len(qu)
            level= []
            for i in range(r):
                cur = qu.popleft()
                if cur:
                    level.append(cur.val)
                    if cur.left:
                        qu.append(cur.left)
                    if cur.right:
                        qu.append(cur.right)
            if len(level)>0:
                out.append(level)
        return out

