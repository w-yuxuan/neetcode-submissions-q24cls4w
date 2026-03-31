# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(n1,n2):
            if bool(n1) + bool(n2) == 1:
                return False
            if bool(n1) + bool(n2) == 0:
                return True

            if n1.val!=n2.val: #most impt check
                return False

            return check(n1.left,n2.left) and check(n1.right,n2.right) #any false causes below runs to not run, no returns = returns none=false
        return check(p,q)