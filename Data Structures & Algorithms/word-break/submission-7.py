class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem = [False]*(len(s)+1)
        mem[len(s)]=True

        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                d = len(w)
                if d <= len(s)-i and w == s[i:i+d] and mem[i+d]==True: # i can fit w here and previous connect point is true
                    # mem[i:i+d]=[True]*d
                    mem[i]=True
                    # continue
                    break

        return mem[0]
            
        

        


        