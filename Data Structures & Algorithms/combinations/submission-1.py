class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curr,res = [],[]


        def dfs(i,k,curr,res):
            if k == len(curr):
                res.append(curr.copy()) # reached a leaf node case, qualifies, writie it down
                return
            # if i > n:
            #     return
            
            
            for j in range(i,n+1): 
                curr.append(j)
                # doesn't # include n
                dfs(j+1,k,curr,res)
                curr.pop()
            
            #dfs(i+1,k,curr,res)
            #there is no case where we include [empty set]

        dfs(1,k,curr,res)
        
        return res