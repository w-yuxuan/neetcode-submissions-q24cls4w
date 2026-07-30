class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem = {}
        def dfs(i):
            if i in mem:
                return mem[i]
            if i>len(s)-1:
                mem[i]=True
                return True
            for w in wordDict:
                d = len(w)
                if s[i:i+d] == w:
                    if dfs(i+d):
                        mem[i+d] = True
                        return True
            mem[i]=False
            return False
        return dfs(0)


            
