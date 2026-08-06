class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res,res2 = [],[]
        a,b = newInterval[0],newInterval[1]
        f1,f2 = 1,0
        # q = deque(intervals)
        
        # while q:
        #     c,d = q.popleft()
        for c,d in intervals:
            if a<= c <= b:
                if d > b:
                    b = d
            elif a<= d <= b:
                if c < a:
                    a = c
            elif c <= a <=b <= d:
                f1 = 0
                res.append((c,d))
            else:
                res.append((c,d))
        if f1:
            res.append((a,b))
        heapq.heapify(res)
        while res:
            j,k = heapq.heappop(res)
            res2.append([j,k])

        return res2