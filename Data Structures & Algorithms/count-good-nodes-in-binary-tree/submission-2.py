# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # plan 1: travel to each node and keep the larges val we have seen in dfs
        
        if not root:
            return 0
        res = 1
        curmax = root.val

        def dfs(root,curmax):
            nonlocal res
            if root.right:
                newmax = curmax
                if root.right.val >= newmax:
                    newmax=root.right.val
                    res+=1
                dfs(root.right,newmax) # if one node fails, all its children also 
            if root.left:
                newmax = curmax
                if root.left.val >= newmax:
                    newmax=root.left.val
                    res+=1
                dfs(root.left,newmax) 
            return
        dfs(root,curmax)
        return res