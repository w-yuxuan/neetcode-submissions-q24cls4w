class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #when the R - L - maxfreq <= k then the R-L is valid
        #pull l only one step towards r when invalid
        di = {}
        l = 0
        r = 0
        maxres = 0 
        maxfreq=0
        # if len(s)
        #R L two pointer
        while l <= r <= len(s)-1 :
            
            #base case#########

            di[s[r]] = di.get(s[r],0)+1
            maxfreq = max(maxfreq,di[s[r]])
            length = r-l+1

            if length-maxfreq <= k: # current window is valid, compare and record 
                maxres = max(maxres,length)

            else :
                di[s[l]] -=1
                l+=1 #not valid, shrink by 1 and recheck if valid
            r+=1   
        return maxres

        










