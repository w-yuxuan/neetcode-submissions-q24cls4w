# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[int]:
        q = deque() # of nodes
        res = [] # of node.val
        if root:
            q.append(root)

        def bfs(node) :#only go one level down for each node:and to rersult and add to search queue
            while q:
                cur = []
                for i in range(len(q)):
                    n = q.popleft()
                    if n:
                        cur.append(n.val)
                        if n.left:
                            q.append(n.left)
                        if n.right:
                            q.append(n.right)
                #level+=1
                res.append(cur)
            return                
        bfs(root)
        return res
