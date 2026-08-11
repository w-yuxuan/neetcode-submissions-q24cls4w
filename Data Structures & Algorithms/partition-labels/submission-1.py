class Solution:
    def partitionLabels(self, s: str) -> List[int]:
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
            prev = -1 # previous string end position
            i = 0
            far = 0 # farthest i need to iter to so far

            while i < len(s):
                far = max(far,pos[s[i]])
                if i==far or i == len(s)-1:
                    res.append(i-prev)
                    prev = i
                # else:
                    
                i+=1

            return res