class Solution:
    def partition(self, s: str) -> List[List[str]]:
        cur,grp,res = '',[],[]

        def check(st):
            l ,r = 0,len(st)-1
            #
            while l<r and st[l] == st[r]:
                r-=1
                l+=1
            return True if l>=r else False 

        def dfs(i,cur,grp):
            if i > len(s)-1:
                if check(cur):
                    grp.append(cur)
                    res.append(grp.copy())
                    grp.pop()
                return

            if check(cur):
                grp.append(cur) # can't continue to add, record this and move on to use the new digit as a new start  
                dfs(i+1,s[i],grp)
                grp.pop()

            cur = cur +s[i]
            dfs(i+1,cur,grp)
            return

        dfs(1,s[0],[])
        return res


        

