# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        flag = True
        def dfs(node):
            nonlocal flag
            if not node: return 0
            if abs(dfs(node.left)-dfs(node.right))>1:
                flag = False 
            return 1+max(dfs(node.left),dfs(node.right))
        dfs(root)
        return flag


         

        
        