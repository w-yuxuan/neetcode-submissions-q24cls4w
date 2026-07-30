# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(n,l,r):
            if n.val <= l or n.val >= r:
                return False
            if n.right:
                if not dfs(n.right,max(l,n.val),r): 
                    return False
            if n.left:
                if not dfs(n.left,l,min(r,n.val)):
                    # now i have new node, everything on the right need to be bigger than the largest of them all
                    return False
            return True
        return dfs(root,float('-inf'),float('inf'))
