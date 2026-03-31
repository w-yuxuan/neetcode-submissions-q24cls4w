class Solution:
    def longestPalindrome(self, s: str) -> str:
        leng = 0
        start = 0
        for i in range(len(s)):
            l,r=i,i

            while l>=0 and r<len(s) and s[l]==s[r]:
                if r+1-(l)>leng:
                    start=l
                    leng = r-l+1
                r+=1
                l-=1
            
            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if r+1-(l)>leng:
                    start=l
                    leng = r-l+1
                r+=1
                l-=1
        return s[start:start+leng]