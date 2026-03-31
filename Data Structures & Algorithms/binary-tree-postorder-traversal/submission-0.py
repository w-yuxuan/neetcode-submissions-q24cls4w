# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Definition for a binary tree node.

        res = []
        if not root:
            return []
        def dfs(n):

            if n.left:
                dfs(n.left) 
            
            if n.right:
                dfs(n.right)
            res.append(n.val)
            
            return
        dfs(root)
        return res