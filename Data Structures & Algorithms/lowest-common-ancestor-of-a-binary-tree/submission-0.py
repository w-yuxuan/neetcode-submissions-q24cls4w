# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pl=[]
        ql=[]
        
        def search1(root,p,pl):
            if root==None: return
            if p == root or search1(root.right,p,pl) or search1(root.left,p,pl):
                pl.append(root)
                return True
        

        def search2(root,q,ql):
            if root==None: return
            if q == root or search2(root.right,q,ql) or search2(root.left,q,ql):
                ql.append(root)
                return True
        
        search1(root,p,pl)
        search2(root,q,ql)

        check = min(len(ql),len(pl))
        pl.reverse()
        ql.reverse()          
        i=0
        lca=None
        while i<len(pl) and i <len(ql):
            if pl[i]==ql[i]:
                lca=pl[i]
                i+=1
            else: break
        return lca            