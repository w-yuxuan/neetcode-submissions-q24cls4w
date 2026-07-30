import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l,r = 1,max(piles)
        # while tot>h:
        while l<r:
            tot = 0
            mid = (l+r)//2
            for p in piles:
                tot+=math.ceil(p/mid)
            if tot > h:
                l = mid+1
            # elif tot == h:
            #     return l
            else: r = mid
        return l

            
        # one function decides whcih side to search
        # one function searches
            
            
