
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #if i build and pop n times, it's k nlogn
        #if i use heap_largest:it's pushing n items one by one onto fixed 
        l=heapq.nlargest(k,nums)
        return l[-1]
