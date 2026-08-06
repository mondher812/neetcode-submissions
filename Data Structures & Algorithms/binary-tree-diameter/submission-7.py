class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # This variable will store the best diameter we've seen so far
        self.max_diameter = 0

        def get_height(node):
            if not node:
                return 0
            
            # Recursively find the height of left and right children
            left_h = get_height(node.left)
            right_h = get_height(node.right)
            
            # UPDATE: The diameter at THIS node is left_h + right_h
            # We compare it against our record holder
            self.max_diameter = max(self.max_diameter, left_h + right_h)
            
            # RETURN: The height of this node to its parent
            return 1 + max(left_h, right_h)

        get_height(root)
        return self.max_diameter