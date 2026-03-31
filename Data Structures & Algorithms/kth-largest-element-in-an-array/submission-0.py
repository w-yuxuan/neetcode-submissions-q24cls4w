class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        #do i have to find heap for all n: cost n
        #if i heapify k and keep pushing till k=N
        #i need N log N to do that if k is small or larte
        if k >= len(nums):
            return nums[0]