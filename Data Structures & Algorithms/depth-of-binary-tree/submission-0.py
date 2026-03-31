class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #1. can count len and double n from 1 each time to see 
        #how many times we double it till it is >= len(root). O(n)
        #2. can search left and right, anyone True then keep +=1
        #if root is not:
        
        if not root:
            return 0
        return 1+ max(self.maxDepth(root.left),self.maxDepth(root.right))
