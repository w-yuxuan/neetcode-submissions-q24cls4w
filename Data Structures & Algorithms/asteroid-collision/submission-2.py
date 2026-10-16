class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        lst = asteroids
        
        res = []
        while True:
            i, j= 0,1
            n = len(lst)
            while i<j<n:
                if lst[i] >0 and lst[j] < 0:
                    tot = lst[i]+lst[j]
                    if tot ==0:
                        i= j+1
                        j= j+2
                    elif abs(lst[i]) > abs(lst[j]):
                        # res.append(lst[i])
                        j+=1
                    else:
                        # res.append(lst[j])
                        # res.append(lst[i])
                        i = j
                        j+=1
                else:
                    #same sign
                    res.append(lst[i])
                    # res.append(lst[j])
                    i = j 
                    j+=1
            if i<n:
                res.append(lst[i])
            if j< n : 
                res.append(lst[j])
            if len(res)==1:
                return res
            if res == lst:
                break
            lst = res.copy()
            res = []
        return res
        
