import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #check length >1
        # s = re.findall(r'\ba-zA-Z+\b',s.lower())
        s = re.sub(r'[^a-zA-Z0-9+]','',s.lower())
        n=len(s)
        if n==1: return True
        #can do 2 pointer since we want full string to be palindrome, not checking the longest sub sequence
        l,r = 0,n-1
        while l<r:
            if s[l]!=s[r]:return False
            l+=1
            r-=1
        return True

