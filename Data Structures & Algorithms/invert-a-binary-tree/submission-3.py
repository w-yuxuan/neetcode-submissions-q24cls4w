class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        l=root.left
        r=root.right
        root.right,root.left = l, r
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root