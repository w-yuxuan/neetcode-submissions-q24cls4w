class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #after hint: create a hash for 26 letters, slide a window of size len(s1) in s2
        # see if any of the substring's hash matches the s1 hash
        if len(s1) > len(s2):
            return False

        h1 = [0]*26
        for i in range(len(s1)):
            h1[ord(s1[i]) - ord('a')] +=1
        
        h2 = [0]*26 
        j=0 
        k = j+len(s1)-1
        for p in range(j,k+1):
            h2[ord(s2[p]) - ord('a')] +=1
        if h2 == h1: return True

        while k <= len(s2)-2:
            # 1. Remove the character at the current j (the one about to be left behind)
            h2[ord(s2[j]) - ord('a')] -= 1
            
            # 2. Move both pointers
            j += 1
            k += 1
            
            # 3. Add the character at the new k
            h2[ord(s2[k]) - ord('a')] += 1
            
            # 4. Compare
            if h2 == h1: return True
        return False 



