# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        if not root:
            return []
        def dfs(n):
            if n.left:
                dfs(n.left) 
            res.append(n.val)
            if n.right:
                dfs(n.right)
            return
        dfs(root)
        return res
            
