class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        d = dictionary
        # res = float('inf')
        n = len(s)
        mem = {}
        def dfs(i): # starting index
            res = float('inf')
            if i in mem:
                return mem[i]
            if i==n:
                return 0
                
            # can always choose to skip a letter
            res = 1+dfs(i+1)

            for word in d:
                leng = len(word)
                if s[i:i+leng] == word:
                    res = min(res,dfs(i+leng))

            mem[i] = res
            return res
                
                # can always choose to skip a letter, 
        return dfs(0)
                