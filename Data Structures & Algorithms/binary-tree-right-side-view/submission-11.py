# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q1,q2 = deque(),deque()
        cur = root
        if cur:
            q1.append(cur)
        else: return []
        while q1:
            cur = q1.popleft()
            if cur.left:
                q2.append(cur.left)
            if cur.right:
                q2.append(cur.right)
            if not q1:
                res.append(cur.val) # current level is done processing
                if q2:
                    q1=q2.copy()# move the next level up to process
                    q2 = deque()
                else:
                    return res
         

        



        

        


