class KthLargest:
    #8th largest is smallest in the first 9

    def __init__(self, k: int, nums: List[int]):
        self.k = k #a ranking so not -1*k
        self.nums=nums
        if self.nums:
            heapq.heapify(self.nums)
            while len(self.nums) > self.k:
                heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val)
        if len(self.nums) > self.k: 
            # don't pop if finding 2nd largest in [1]
            #you already have it 
            heapq.heappop(self.nums)
        return self.nums[0]
    