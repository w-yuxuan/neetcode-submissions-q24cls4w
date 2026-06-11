# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return []
        else: res.append(root.val)
        one = deque()
        two = deque()

        one.append(root)
        while one or two:
            while one:
                n = one.popleft()
                if n.left:
                    two.append(n.left)
                if n.right:
                    two.append(n.right)
            if two:
                res.append(two[-1].val)
            one = two.copy()
            two = deque()
        
        return res
        

        
