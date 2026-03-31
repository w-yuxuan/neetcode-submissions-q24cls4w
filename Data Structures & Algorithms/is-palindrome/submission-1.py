#need to parse out the ?
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)<2:
            return True
        odd=0
        #for i, val in enumerate(s):
        s=re.findall(r'[a-zA-Z0-9]',s)
#        s = s.lower()
        for i in range(len(s)//2):
            
            if s[i].lower() !=  s[-i-1].lower():
                odd += 1
        if odd > 0:
            return False
        else:
            return True


            