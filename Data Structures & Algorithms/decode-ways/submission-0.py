class Solution:
    def numDecodings(self, s: str) -> int:
        ways= 0
        cur = []
  
        if len(s)==1:
            if 0<int(s[0]):return 1
            else: return 0
            
        #either start a new int or continue adding this digit to the last one
        def check(j,i):
            nonlocal ways

            if j>=len(s):
                ways+=1
                return

            for i in range(j+1,len(s)+1): # always move i forward and only move j if adding ith to perv string is not allowed             
                cur = s[j:i]
                if cur.startswith('0'): 
                    return   
                if 0< int(cur) <=26 : # current num is not valid, else keep adding  
                    check(i, 0)    # CORRECT: Moves start index to i
                    #don't return False yet since you can have other paths that make it to the end and add 1 to ways 
                else: # can continue with current j and keep adding to the sequence 
                    break
                # not check(i+1): bc we don't need to check if current a palindrom or anything, we remove the recursion and use loop
        check(0,0)
        return ways if ways!=0 else 0
            
            
             