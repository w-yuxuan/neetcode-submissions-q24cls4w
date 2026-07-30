# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n  = root
        q= deque()
        while n or q:
            while n:
                q.append(n)
                n = n.left
            n = q.pop()
            k-=1
            if k == 0 :
                return n.val
            n = n.right
        
                