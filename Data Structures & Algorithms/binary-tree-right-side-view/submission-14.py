# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: #18
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q= deque()
        if root:
            q.append(root)
        else:return []

        while q:
            res.append(q[-1].val)
            for i in range(len(q)):
                n = q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        return res

        

        
