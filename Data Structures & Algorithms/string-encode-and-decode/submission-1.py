class Solution:

    def encode(self, strs: List[str]) -> str:
        # plan 1: use the ord() as the hashmap to map a string to
        # after hint:
        res = ''
        for s in strs:
            res += str(len(s))+'#'+s
        return res
    def decode(self, s: str) -> List[str]:
        # plan one: inner loop finds #, takes what's before it as the len, and takes that len to pop the s and store that as a substring
        res = ''
        
        i=0
        start = 0 # start of the first text sgement
        count = 0 
        res = []
        while i <= len(s)-1: #pointer for what we are currently processing
            
            if s[i] != '#':
                count +=1
                i+=1
            else: 
                l = int(s[start:start+count])
                seg = s[start+count+1:start+count+1+l]  #[ #digits of the count, +1 for '#' + count]
                
                start += 1+count+l
                i= start #fast forward i past the l text, since it alread walked through the # and the length denoter
                
                res.append(seg)
                count = 0 

        return res
        
        
