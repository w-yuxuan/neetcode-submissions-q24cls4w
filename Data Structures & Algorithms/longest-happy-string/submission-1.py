class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        h = [(-cnt,lett) for (cnt,lett) in [(a,'a'),(b,'b'),(c,'c')] if cnt != 0]
        # prune so i won't need to check if the cnt is 0 later before decrement -1 
        heapq.heapify(h)
        res = []

        while h:
            cnt,lett = heapq.heappop(h)
            #check 3 in a roll
            if len(res)>=2 and res[-1]==res[-2]==lett:
                if h: #still have second highest count one i can pop
                    cnt2,lett2 = cnt,lett
                    cnt,lett = heapq.heappop(h)
                    heapq.heappush(h,(cnt2,lett2))
                else:
                    return ''.join(res)
            res.append(lett)
            if cnt+1 < 0:
                heapq.heappush(h,(cnt+1,lett))
        return ''.join(res)

        

            
