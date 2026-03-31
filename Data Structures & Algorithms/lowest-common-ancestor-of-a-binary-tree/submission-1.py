class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = None
        #res = [False,False]
        def find(root):
            nonlocal lca
            if not root:
                return [False,False]
            if lca : 
                return [False,False] 
            left=find(root.left)
            right=find(root.right)

            res= [(p==root) or left[0] or right[0], (q==root) or left[1] or right[1]]          
           
            if res[0] and res[1] and not lca:
                lca = root
            return res
        find(root)
        return lca   