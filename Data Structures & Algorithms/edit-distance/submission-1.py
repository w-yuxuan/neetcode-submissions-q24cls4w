class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # abort anytime the op count is larger than word len.
        # at ea pt i have 3 choices
        w1,w2 = word1,word2
        l1,l2 = len(w1),len(w2)

        mem = {}
        # only delete when 1 matches with 2's next lett
        # only add when their next letter match
        def dfs(i,j):
            if i==l1:
                if j==l2:
                    return 0
                else:
                    return l2-j # add the rest of w2
            if j==l2:
                return l1-i # delete the rest of w1
            
            if (i,j) in mem:
                return mem[(i,j)]

            if w1[i]==w2[j]:
                mem[(i,j)] =dfs(i+1,j+1)
                return mem[(i,j)]

            res = max(l1,l2)
            # always can do the replacement
            res = min(res,dfs(i+1,j+1)+1)

            # can always run delete/add to resolve len mismatch
            if l1-i >= l2-j: # have more l1 left, delete from i
                res = min(res,dfs(i+1,j)+1)
            if l1-i <= l2-j: # have less l1 , add to i
                res = min(res,dfs(i,j+1)+1)
                
            mem [(i,j)] = res
            return res
        return dfs(0,0)


            # if i<l1:
            #     if w1[i+1]=w2[j]: # delete from i
            #         res = min(res,dfs(i+1,j)+1)

            #     if j<l2:
            #         #both have letters left
            #         if w1[i+1]=w2[j+1]: # can 

                    
            

