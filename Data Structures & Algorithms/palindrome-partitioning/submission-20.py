class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []

        def check(st):
            l ,r = 0, len(st)-1
            while l<=r and st[l]==st[r]:
                l+=1
                r-=1
            return l>=r

        def dfs(i,cur):
            if i>len(s)-1:
                res.append(cur.copy())
                return

            # for i in range(len(s)):
            for j in range(i+1,len(s)+1): # one beyond the actual stopping point 
                if check(s[i:j]):
                    cur.append(s[i:j])
                    dfs(j,cur)
                    cur.pop()
                # dfs(i+1,[])
            # always explore splitting to a new palin
        
        dfs(0,[])
        return res