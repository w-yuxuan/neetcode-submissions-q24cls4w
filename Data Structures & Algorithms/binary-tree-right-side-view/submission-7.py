# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # keep adding to stack and going right, record the number of levels we went down
        #if no right then go left once, if no left no right: stop
        #
        # then process the left side tree, do the same thing, if left side levels broke right side, then start adding to the result
        res = []
        left = []
        r = l = 0
        def find(root,res,h):
            while root:
                res.append(root.val)
                h +=1
                if root.right:
                    root = root.right
                elif root.left:
                    root= root.left
                else: return h

        r_height = find(root,res,r)
        if root and root.left:
            l_height = find(root.left,left,l)+1
            if r_height < l_height:
                res.append(left[r_height-1])
        return res
            
