class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # n log n to order, + n/2 pair comparisions , vs n^2 comparisons
        s = sorted(intervals,key=lambda x: x[0])
        res = []
        # can't keep popping the og list since that will change the indexing as we read it as input for later layers

        if len(s)==1:
            return s
        q = deque(s)
        a,b = 0,1
        cur = s[0]

        while q:
            new = q.popleft()

            if cur[1]< new[0]:
                res.append(cur)
                cur = new
            #else intersect 
            cur[0] = min (cur[0],new[0])
            cur[1] = max(cur[1],new[1])
        res.append(cur)
        return res
