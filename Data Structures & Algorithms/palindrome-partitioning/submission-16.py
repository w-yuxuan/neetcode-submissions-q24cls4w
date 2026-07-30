class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def check(st):
            return True if st == st[::-1] else False
        
        def dfs(l,cur):
            if l>len(s)-1:
                res.append(cur.copy())
                return

            for r in range(l,len(s)):
                st = s[l:r+1]
                if check(st):
                    cur.append(st)
                    dfs(r+1,cur)
                    cur.pop()
            return 
        dfs(0,[])
        return res