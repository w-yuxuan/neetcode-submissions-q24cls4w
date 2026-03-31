#repeat
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
 
        #intialize
        bank = set()
        L = 0
        #iterate through each point
        for R in range(len(s)):
        #if i find someone in the set i pull L up until i fix it 
            while s[R] in bank:
                bank.remove(s[L])
                L += 1
            
            bank.add(s[R])
            longest = max(longest,R-L+1)
        return longest        
