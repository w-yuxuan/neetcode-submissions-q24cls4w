# me trying neetcode approach, sml err can you spot them

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        # plan 1: travel to each node and keep the larges val we have seen in dfs
        def dfs(node,curmax): # output the sum so far
            nonlocal res
            if not node:
                return 0
            if node.val >= curmax:
                curmax = node.val
                res=1
            else: res = 0
            res += dfs(node.right,curmax)
            res += dfs(node.left,curmax)
            return res
        dfs(root,root.val)
        return res