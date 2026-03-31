# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        bal = True

        def check(node):# gets depth of current node, passes it upstairs, and checks if node is unbal 
            nonlocal bal
            if not node:
                return 0
            if abs(check(node.left)-check(node.right))>1:
                bal=False         
            return 1+max(check(node.left),check(node.right))

        check(root)
        return bal


            
         

        
        