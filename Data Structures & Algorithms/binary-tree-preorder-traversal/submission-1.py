# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        cur = root
        res = []
        while cur or stack:
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                cur = cur.left
            elif stack:
                cur = stack.pop() 
            else: break          
        return res