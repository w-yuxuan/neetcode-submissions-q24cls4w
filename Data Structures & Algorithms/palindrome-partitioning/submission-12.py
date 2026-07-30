class Solution:
    def partition(self, s: str) -> List[List[str]]:
                #skip duplicates 

        def palin(s):
            l,r = 0, len(s)-1
            while l<r:
                if s[l]==s[r]:
                    l+=1
                    r-=1
                else: return False
            return True
        
        cur = []
        res = []
        def dfs(j,i):
            test = s[j:i+1]
            nonlocal cur,res
            if i > len(s)-1:
                if j==i and cur:# so that only "cur results" from dfs(i+1,i+1) branch gets recorded, not from the branch when we just keep moving the RHS
                    res.append(cur.copy())
                return
            
            # check if I include ith letter if it's a palin
            # cur.append(s[i])
            # if palin(cur):
            #     res.append(cur)
            #     cur.pop()
            
            if palin(test):
                cur.append(test) # still a palin, so keep adding on letters and add to result later
                dfs(i+1,i+1)
                cur.pop()
            # cur.append(test)
            dfs(j,i+1)
            return
        dfs(0,0)
        return res
