class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dum way: 
        
        # create heap of size k 
        c = Counter(nums)
        s = []
        heapq.heapify(s)
        res = []
        high = 0
        
        inv = defaultdict(list)

        for key,val in c.items():
            high = max(high,val)
            inv[val].append(key)

        kk = 0
        cc = high
        while kk < k and 0<cc:
            if cc in inv:
                res.extend(inv[cc])
                kk+=len(inv[cc])
            cc-=1
        return res
            


        
