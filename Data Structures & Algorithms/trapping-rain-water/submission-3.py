class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)==1:
            return 0
        res = 0

        for i in range(len(height)):
            hl = height[i]
            hr = height[i]
            for l in range(0,i):
                if height[l]> hl:
                    hl = height[l]

            for r in range(i+1,len(height)):
                if height[r] > hr:
                    hr = height[r] 
            res += max(min(hl,hr)-height[i] , 0)

        return res