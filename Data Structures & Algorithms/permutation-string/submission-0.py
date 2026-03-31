class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #after hint: create a hash for 26 letters, slide a window of size len(s1) in s2
        # see if any of the substring's hash matches the s1 hash
        if len(s1) > len(s2):
            return False

        h1 = [0]*26
        for i in range(len(s1)):
            h1[ord(s1[i]) - ord('a')] +=1
        
        
        for j in range(len(s2)):
            h2 = [0]*26
            k = j+len(s1)-1
            if k > len(s2)-1:return False
            for p in range(j,k+1):
                h2[ord(s2[p]) - ord('a')] +=1
            if h2 == h1: return True
        return False 



