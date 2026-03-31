class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #plan 1: try numbers and calculate the time it takes for each pile by /2 round up, and then sum to compare with h
        # hint:
        # prev i was wrong: thinking upper bound is not  max(piles) / 2  but 2nd largest if i want to be done >= h+1 steps
        
        #starting val
        maxi= max(piles)

        #try to finish in ranges that are : both sides inclusive
        def test(l,r):
            k = math.floor((r+l)/2)   #not r-l         
            tot = 0

            if l==r:
                return k
            for i in piles:
                tot += math.ceil(i/k)
            if tot <= h: # k too large
                return test(l,k) # not k-1
            elif tot > h:
                return test(k+1,r)
            return 
        return test(1,maxi)
