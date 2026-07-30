class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem = [False]*(len(s)+1)
        mem[-1] = True
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                d = len(w)
                if i+d <= len(s) and s[i:i+d] == w:
                    if mem[i+d]:
                        mem[i] = True
                        break
        return mem[0]

            
