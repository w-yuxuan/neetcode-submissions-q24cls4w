# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#[1,3,2 ]
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        s = deque([])
        
        res= []
        if not root: 
            return res
        else:
            res.append([root.val])
            s.append(root)
        
        while s:
            cur = []
            for i in range(len(s)):
                node = s.popleft()
                if node.left:
                    s.append(node.left)
                    cur.append(node.left.val)
                if node.right:
                    s.append(node.right)
                    cur.append(node.right.val)             
            if cur:
                res.append(cur)
        return res
