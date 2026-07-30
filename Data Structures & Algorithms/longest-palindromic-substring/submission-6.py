class Solution:
    def longestPalindrome(self, s: str) -> str:
        lgst = 0
        res = ''
    
        for i in range(len(s)):
            #odd
            l = i 
            r = i
            while 0 <= l <=r <= len(s)-1 and s[l]==s[r]:
                if r-l+1 > lgst:
                    lgst = r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1

            #even
            l=i
            r=i+1

            while 0 <= l <=r <= len(s)-1 and s[l]==s[r]:
                if r-l+1 > lgst:
                    lgst = r-l+1
                    res = s[l:r+1]
                l-=1
                r+=1

        return res


