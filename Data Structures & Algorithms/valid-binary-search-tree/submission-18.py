class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(root, minn, maxx):
            if not root:
                return True

            if not (minn < root.val < maxx):
                return False

            return (
                valid(root.left, minn, root.val) and
                valid(root.right, root.val, maxx)
            )

        return valid(root, float("-inf"), float("inf"))