class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)==1:
            return 0
        res = 0

        mem = [[height[0],height[-1]] for _ in range(len(height))]

        hr=0
        hl= 0
        for i in range(len(height)-1):
            hl = max(height[i],hl)
            mem[i][0] = hl

        for i in range(len(height)-1,-1,-1):
            hr =  max(height[i],hr)
            mem[i][1] = hr
                    
        for i in range(len(height)):
            hl,hr = mem[i] 
            res += max(min(hl,hr)-height[i] , 0)

        return res