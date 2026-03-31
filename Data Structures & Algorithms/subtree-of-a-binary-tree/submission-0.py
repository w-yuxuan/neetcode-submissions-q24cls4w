class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #key during root comparison phase : 
        # FF T, FT F, TT compare, not equal means F, TF F
        #and searching for the next potential branch/root to compare phase 
        #  FF T(once return we don't continue), FT F, TT compare, not equal means continue, TF F
        # if you see a none node, stop there

        #key diff btw searhcing and actual comparision: 
        # during search, no match means i can move on 
        #if node=none i stop
        
        #why we need to separate out None cases?
        #n.val can't execute 
        def search(r,s):
            
            #order matters! no s must be T, regardless of r, so put that first
            if not s:
                return True
            
            if not r:
                return False
            
            #root , no sub

            
            #########root and sub exist
            # no need to :if r and s: that's the only case left
            #if either side subtree works, return T to outer most
            
            #if same(r.left,s.left) or same(r.right,s.right) :err bc I should start checking this node
            if same(r,s):
                return True
            

            # i want to keep recursing for my children, incase the 
            # imediate l and r are the only ones that don't match, their
            #children match. 

            # i need to involve both ll and rr comparisions
            #if i do "if statement: return T", then somtimes it returns nothing
            #but how do i include the two sides in one return line?

            #return search l l and /or search r r? wrong logic
            #that's right! if either r or l side==T, then "same"must have worked,
            #the only other way was "not r", which would have given T as node1
            return search(r.left,s) or search(r.right,s)

        
        # forgot to check none's. didn't we make sure that both T upstairs?Ans below
        #def same(r,s):
        #     if r.val == s.val:
        #         return same(r.left,s.left) and same(r.right,s.right)
        #     return False
        # return search(root,subRoot)

        #we make sure that both T upstairs, but need to check levels below that when we recurse
        #difference from last fcn ?
        def same(r,s):
            if not r and not s:
                return True
            if not r and s or not s and r:
                return False
            if r.val == s.val:
                return same(r.left,s.left) and same(r.right,s.right)    
            return False #for both exist, val not equal 

        # can't gen'lize "not s" as T like last time when we treat the 1st node comparison
        #now r but not s means they are not the same! 
        return search(root,subRoot)