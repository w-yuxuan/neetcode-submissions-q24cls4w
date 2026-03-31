class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0 
        bank = set()
        maxL = 0 
        for R in range(len(s)) :
            while s[R] in bank:
                bank.remove(s[L])
                L+=1
            bank.add(s[R])

            maxL = max(maxL,R-L+1)
        return maxL
