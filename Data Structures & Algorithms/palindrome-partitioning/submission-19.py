class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def check(st):
            l,r = 0,len(st)-1
            while l<r and st[l] == st [r]:
                l+=1
                r-=1
            return True if l>=r else False
        
        def dfs(i,cur):
            if i>len(s)-1:
                res.append(cur.copy())
                return 
            
            for j in range(i+1,len(s)+1):
                new = s[i:j]
                if check(new):
                    cur.append(new)
                    dfs(j,cur)
                    cur.pop()
        dfs(0,[])
        return res