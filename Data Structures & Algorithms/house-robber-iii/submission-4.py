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
            if n in mem:
                return mem[n]
            if not n:
                return [0,0]
            skip=0
            keep = n.val
            if n.left:
                skip += max(dfs(n.left))
                keep += dfs(n.left)[0]
            if n.right:
                skip += max(dfs(n.right))
                keep += dfs(n.right)[0]
            mem[n]=[skip,keep]
            return [skip,keep]
        return max(dfs(root))
