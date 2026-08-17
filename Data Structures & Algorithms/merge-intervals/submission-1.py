class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        s = sorted(intervals,key=lambda x: x[0])
        if len(s) == 1:
            return intervals
        a ,b = 0, 1
        cur = s[0]
        res= []
        while a < len(s):
            if s[a][0] > cur[1]: # new one don't interfere
                res.append(cur)
                cur = s[a]
            else:
                #interfere
                cur[0] = min(cur[0],s[a][0])
                cur[1] = max(cur[1],s[a][1])
            a+=1
        res.append(cur)
        return res
