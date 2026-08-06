# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.counter = 0
        def dfs(node,cm):
            if node is None:
                return 
            new_m = cm
            if node.val >= cm:
                self.counter+=1
                new_m = node.val

            dfs(node.right,new_m)
            dfs(node.left,new_m)
        if root:
            dfs(root,root.val)

        return self.counter