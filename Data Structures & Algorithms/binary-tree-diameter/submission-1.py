class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        lgst= 0
        def search_oneside(root): #actually root should be called node
            if not root:
                return 0
            #since from top to bottom there is always a path = n(levels )-1 long
            #i need to negative one from the total num levels
            # doing it on the bottom level is easiest

            
            else:
                l=search_oneside(root.left)
                r=search_oneside(root.right)
                nonlocal lgst
                if l+r > lgst:
                    lgst = l+r
                
                return 1+max(l,r)
        search_oneside(root)
        return lgst