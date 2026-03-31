class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        # push a max of k items onto it 
        # ea one comes after tthat we push then pop
        while len(h) < k and nums:
            heapq.heappush(h,nums.pop())
        while nums:
            heapq.heappush(h,nums.pop())
            heapq.heappop(h)
        res = heapq.heappop(h)
        return res


