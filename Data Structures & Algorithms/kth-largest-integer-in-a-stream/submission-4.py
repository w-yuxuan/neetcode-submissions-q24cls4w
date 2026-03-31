
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        #above gives same heap as my prev method

    def add(self, val: int) -> int:
        #diff is here: they always push first, then decide if to pop based on length. incase k was > len(nums)
        heapq.heappush(self.nums,val)
        if self.k < len(self.nums):
            heapq.heappop(self.nums)
        return self.nums[0]