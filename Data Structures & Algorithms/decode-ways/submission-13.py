class Solution:
    def numDecodings(self, s: str) -> int:
        # looks like a  palindrome partiion q
        # every time i hit the last one i add one 
        mem = {}
        def check(st):
            if st[0]=='0':
                return False
            if int(st)<=26:
                return True
   
        def dfs(i):
            # nonlocal res
            res = 0
            if i in mem:
                return mem[i]
            if i > len(s)-1:
                # res +=1
                return 1
            for j in range(i,i+2):
                if j > len(s)-1:
                    break
                new = s[i:j+1]
                if check(new):
                    res += dfs(j+1)
            mem [i]=res
            return res
            
        return dfs(0)
        # return res 


            


            

