class Solution:
    def countSubstrings(self, s: str) -> int:
        #even cases
        n = len(s)
        count=0
        if n==1:
            return 1
        for i in range(n):
            l=r=i
            while 0 <= l <= r <= n-1:
                if  s[l]==s[r]:
                    count+=1
                else:
                    break
                l-=1
                r+=1
            #reset to test odd cases
            l=i
            r=i+1
            while 0 <= l < r <= n-1:
                if  s[l]==s[r]:
                    count+=1
                else:
                    break
                l-=1
                r+=1
        return count
            


        # def palin(s):
        #     return
        
        