class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        i = 0
        h = []
        heapq.heapify(h)
        while i<=len(nums)-1 and i<k:

            heapq.heappush(h,nums[i])
            i+=1
        while i<=len(nums)-1:
            if h[0] < nums[i]:
                heapq.heappop(h)
                heapq.heappush(h,nums[i])
            i+=1
        return h[0]
