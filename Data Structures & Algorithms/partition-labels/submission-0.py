class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # dumb: 2^n way of either starting a new string or continuing 
        # n: start from each pt and wrtie down where that char was next observed and cut the string there. if you have seen another new char in between, make sure you keep going till you find a pair for it also.
        #how to implement: if i append to string then remove it that is n*n for search
        search = False
        res = []
        mem = defaultdict(int)
        pos = defaultdict(int)
        for i in range(len(s)):
            mem[s[i]]+=1
            pos[s[i]] = i # last seen position
        for num in mem.values():
            if num >=2 :
                search = True
            else: res.append(1) # accumulate 1's if i keep finding single occurances
        
        if not search:
            return res
        else:
            res = []
            d = defaultdict(int)
            cur = 0 #current string len
            prev = -1 # previous string end position
            i,j = 0,1
            far = 0 # farthest i need to iter to so far

            while i < len(s):
                far = max(far,pos[s[i]])
                if i==far or i == len(s)-1:
                    res.append(i-prev)
                    prev = i
                # else:
                    
                i+=1

            return res


                # while j > i: 
                #     j = pos[s[i]]

                #     new = pos[s[i]]-prev+1
                #     cur = max(cur,pos[s[i]]-prev+1)

                # if pos[s[i]] == len(s)-1: # else we reached the end
                #     res.append(cur)
                #     return res
                # i+=1
                






            
        
