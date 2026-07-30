class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        mem = {}
        def check(i):
            if i in mem:
                return mem[i]
            if i >= len(s):
                return True
            
            for w in range(len(wordDict)):
                d = len(wordDict[w])
                if s[i:i+d] == wordDict[w]:
                    if check(i+d):
                        mem[i+d] = True
                        return True
            mem[i+d] = False
            return False
        
        return check(0)