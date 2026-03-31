class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def search(r,s):
            if not s:
                return True
            if not r: #s , no r
                return False
            # s and r
            if same(r,s) == True:
                return True
            
            return search(r.left, s) or search(r.right,s)
        
        def same(r,s):
            if not r and not s:
                return True
            if not r or not s: 
                return False
            if r.val == s.val:
                return same(r.left,s.left) and same(r.right,s.right)
            return False

        return search(root,subRoot)