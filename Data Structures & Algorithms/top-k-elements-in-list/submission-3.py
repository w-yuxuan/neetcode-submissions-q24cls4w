class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dum way: 
        
        # create heap of size k 
        c = Counter(nums)
        s = []
        heapq.heapify(s)
        res = []

        for key,val in c.items():
            heapq.heappush(s, (-val,key))
        
        for i in range(k):
            v,k = heapq.heappop(s)
            res.append(k)
        return res
        
