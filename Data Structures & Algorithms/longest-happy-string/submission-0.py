class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        h = [(cnt,key) for cnt,key in [(-a,'a'),(-b,'b'),(-c,'c')] if cnt!=0 ]
        heapq.heapify(h)
        res = []
        while h:
            cnt,lett = heapq.heappop(h)

            if len(res)>=2 and res[-1]==lett and res[-2] == lett: #over the limit
                cnt2,lett2 = cnt,lett
                if h:
                    cnt, lett= heapq.heappop(h)
                    heapq.heappush(h,(cnt2,lett2)) # push the one we can't use back on
                else: # no more alternative ones to buffer from the 3 in a role case, this is the longest
                    break
            res.append(lett)
            if cnt+1<0:
                heapq.heappush(h,(cnt+1,lett))
        return ''.join(res)



