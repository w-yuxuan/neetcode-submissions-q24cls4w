class Solution:
    def trap(self, height: List[int]) -> int:
        #check if only 1 item

        hl,hr = height[0],height[-1]
        l = 0
        r = len(height)-1

        res = 0

        while 0<= l<r <= len(height)-1:
            hl = max(height[l],hl)
            hr = max(height[r],hr)
            if hl < hr:
                l+=1
                res += max(min(hl,hr)-height[l] ,0) # calc the water trapped for the place we moved to
            else:
                r-=1
                res += max(min(hl,hr)-height[r],0)
            # update res after moving, we can mentally check the first 2 bars give right result 
        return res





