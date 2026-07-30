# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        if root:
            q.append(root)
            # res.append(root.val)
        while q:
            r = None
            # this section is to handle the root, and also restart after each level 
            # l = q.len()
            l=len(q)
            for i in range(l):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    r = node
            if r:
                res.append(r.val)

        return res
            


         

        



        

        


