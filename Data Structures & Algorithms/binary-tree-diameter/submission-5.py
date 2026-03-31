# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        curmax=0
        def find(node):
            nonlocal curmax
            if not node:
                return 0
                
            if not node.left and not node.right:
                return 0
            elif node.left and node.right: # both side has children, check if the subtree gives the max
                curmax=max(find(node.left)+find(node.right)+2,curmax)
            #else: # only one side 
            
            #always return the longest child +1
            return 1+max(find(node.left),find(node.right)) 
        
        return max(find(root),curmax) # return the longest of :from conncting the longest branch below vs internal loops