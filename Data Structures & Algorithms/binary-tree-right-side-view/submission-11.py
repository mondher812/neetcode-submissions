# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        out= []
        temp = []
        cur_n = root
        if cur_n:
            temp.append(cur_n)
            while len(temp) >0:
                tlen = len(temp)
                right = None
                for i in range(tlen):
                    node = temp.pop(0)
                    if node:
                        right = node
                        temp.append(node.left)
                        temp.append(node.right)

                if right:
                    out.append(right.val)
        return out





            
           
  

        