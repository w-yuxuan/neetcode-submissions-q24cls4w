class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        lgst = 0
        #d = 
        def depth(node):
            if not node:
                return 0
            
            diam = depth(node.left)+depth(node.right)
            
            nonlocal lgst
            if diam > lgst:
                lgst = diam  
                
            return 1+max(depth(node.right),depth(node.left))


        depth(root)
        return lgst


