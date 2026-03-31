class Solution:
    def trap(self, height: List[int]) -> int:
        store = [[0,0] for i in range(len(height))]
        res = 0
        # handle if only one bar

        hl = hr = 0
        for i,h in enumerate (height):
            hl = max(hl,h)
            # if store[i][0]<hl:
            store[i][0]=hl

        for i,h in enumerate(height[::-1]):
            hr=max(hr,h)
            # if store[::-1][i][1]<hr:
            store[::-1][i][1]=hr   

        for i,h in enumerate (height):
            
            res += max( min(store[i][0],store[i][1])-h , 0)
        return res

     
