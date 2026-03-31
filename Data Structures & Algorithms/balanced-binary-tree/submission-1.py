# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:return True
        #iteratively find depthL-deppthR
        #not a recursive call on itself but above fcn
        #above line wrong: recursively check
        def depth(node):
            if not node: return 0
            return 1+max(depth(node.left),depth(node.right))
        
        if not self.isBalanced(root.right):
            return False
        if not self.isBalanced(root.left):
            return False

        if abs(depth(root.right) - depth(root.left)) >1:
            return False

        return True
            
        

         

        
        