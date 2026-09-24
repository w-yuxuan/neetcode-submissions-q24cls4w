class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        mem = [False]*len(s)
        mem[-1]= (s[-1]=='0')

        for i in range(n-2,-1,-1):
            if s[i]=='0':
                for j in range(i+minJump,min(i+maxJump,n-1)+1):
                    if mem[j]:
                        mem[i]=True
                        break
        return mem[0]
            
