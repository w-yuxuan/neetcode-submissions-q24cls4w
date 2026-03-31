class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        L = 0
        charSet = set()

        for R in range(len(s)):
            # While the new character is ALREADY in our window...
            # We must shrink the window from the left to remove it.
            while s[R] in charSet:
                charSet.remove(s[L])
                L += 1
            
            # Now it is safe to add the new character
            charSet.add(s[R])
            
            # Update the max length
            # Note: It is (R - L + 1), not (L - R + 1)
            res = max(res, R - L + 1)

        return res
