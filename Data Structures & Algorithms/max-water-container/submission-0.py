class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #keep vol as global comparision storage
        m = 0
        l = 0
        r = len(heights)-1
        while r > l:
            area = min(heights[l],heights[r])*(r-l)
            m = max(m,area)
            if heights[l] > heights[r]:
                r-=1
            else: l+=1
        return m
            





