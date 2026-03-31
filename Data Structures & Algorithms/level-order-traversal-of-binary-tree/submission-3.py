# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        if root:
            res = [[root.val]]
        else:
            return []
        while q:
            cur = [] #current level result
            for i in range(len(q)): 
                node = q.popleft()
                if node.left:
                    cur.append(node.left.val)
                    q.append(node.left)
                if node.right:
                    cur.append(node.right.val)
                    q.append(node.right)      
            if cur:
                res.append(cur)
        return res



                
            

            