# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # read then do a heap soln: n + nlogn
        q = deque()
        res = deque()
        def dfs(n):
            while n or q:
                while n:
                    q.append(n)
                    n=n.right
                n = q.pop()
                res.append(n)
                n = n.left
        dfs(root)
        for i in range(k):
            j = res.pop()
        return j.val
