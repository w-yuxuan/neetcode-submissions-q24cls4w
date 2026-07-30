class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # if len(nums) < k:
        #     return nums
        h = []
        heapq.heapify(h)
        for i in range(k):
            heapq.heappush(h,nums[i])
        for j in range(len(nums)-k):
            if h[0] < nums[j+k]:
                heapq.heappop(h)
                heapq.heappush(h,nums[j+k])
                
        return h[0]
            