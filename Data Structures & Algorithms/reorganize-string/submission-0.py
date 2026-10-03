class Solution:
    def reorganizeString(self, s: str) -> str:
        # differnt ways or rearranging then checking : N! x N one time horizontal check
        # pop the most frequent one first 
        h = []
        heapq.heapify(h)
        # cnt = math.counter(s)
        cnt = defaultdict(int)
        for i in s:
            cnt[i]+=1
        
        for k,v in cnt.items():
            heapq.heappush(h,(-v,k))

        last = ''
        res = []
        while h:
            v1,k1  = heapq.heappop(h)
            if k1 != last:
                last = k1
                res.append(k1)
                if v1+1!=0:
                    heapq.heappush(h,(v1+1,k1))
            else:
                v2,k2 = v1,k1
                if h:
                    v1,k1  = heapq.heappop(h)
                    last = k1
                    res.append(k1)
                    if v1+1!=0:
                        heapq.heappush(h,(v1+1,k1))
                    heapq.heappush(h,(v2,k2))
                else:
                    return ''
        return ''.join(res)