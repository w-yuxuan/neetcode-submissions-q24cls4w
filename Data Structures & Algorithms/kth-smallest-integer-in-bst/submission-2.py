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
        def dfs(n):
            if n:
                dfs(n.right)
                q.append(n)
                dfs(n.left)
        dfs(root)
        for i in range(k):
            j = q.pop()
        return j.val
