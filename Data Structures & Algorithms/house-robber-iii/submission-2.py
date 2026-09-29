# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        mem = {}
        def dfs(n):
            if not n:
                return 0
            if n in mem:
                return mem[n]
            res = n.val
            nextlevel = 0
            if n.left:
                res+= dfs(n.left.left)+dfs(n.left.right)
                nextlevel += dfs(n.left)
            if n.right:
                res+= dfs(n.right.left)+dfs(n.right.right)
                nextlevel += dfs(n.right)
            res = max(res,nextlevel)
            mem[n] = res
            return res
        return dfs(root)