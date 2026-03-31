class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums

        #p=self.nums[:k]
        self.p=self.nums[:k]
        #else only local 

        heapq.heapify(self.p)
        if len(nums)>k:
            for i in nums[k:]:
                if i >= self.p[0]:
                    heapq.heappush(self.p,i)   
                    heapq.heappop(self.p) #don't forget to keep only p elements


    def add(self, val: int) -> int:
        if self.k > len(self.p):
            heapq.heappush(self.p,val)
        elif val >= self.p[0]:
            heapq.heappush(self.p,val)
            heapq.heappop(self.p)
        
        return self.p[0]

