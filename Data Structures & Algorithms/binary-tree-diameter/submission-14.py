class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # This variable will store the best diameter we've seen so far
        def getDepth(root):
            max_d = 0
            if root is None:
                return max_d
            else:
                
                max_d=1+max(getDepth(root.left),getDepth(root.right))
                return max_d
        if root is None:
            return 0 
        else:

            maxl = getDepth(root.left)
            maxr = getDepth(root.right)
            d = maxl + maxr
            s = max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
            return max(d,s)





        