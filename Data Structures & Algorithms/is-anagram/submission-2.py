class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len (t):
            return False
        count_s = {}
        count_t = {}

        #for i in len(s): #big err: 
        for i in range(len(s)):
        #    count_s[s[i]] = count_s[s[i]] +1

        # is wrong because if s[i] is not already in count_s, you'll get a KeyError. You need to initialize the count if the key doesn't exist.
        
            count_s[s[i]] = count_s.get(s[i],0) +1
            count_t[t[i]] = count_t.get(t[i],0) +1
        return count_s == count_t