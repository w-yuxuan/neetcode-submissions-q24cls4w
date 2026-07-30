class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # if i do k max heap, then i'll pop off largest
        # i i do min heap, the top is the smalleest 

        h = []
        heapq.heapify(h)
        i = 0
        while k>0:
            heapq.heappush(h,nums[i])
            k-=1
            i+=1
        while i<=len(nums)-1:
            heapq.heappush(h,nums[i])
            heapq.heappop(h)
            i+=1
        return h[0]
        