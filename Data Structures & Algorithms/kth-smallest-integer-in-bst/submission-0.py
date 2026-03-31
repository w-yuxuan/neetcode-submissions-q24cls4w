# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        def search(node):
            if node is None:
                return None
            search(node.left)
            res.append(node.val)
            search(node.right)
            return
        search(root)
        return res[k-1]
