class Solution:
    def findMin(self, nums: List[int]) -> int:

        def find(l,r):
            mid = (l+r)//2
            if r == l:
                return nums[l]
            if nums[mid]<nums[r]: # when two left, l will = mid
                # if r-mid ==1:
                #     return nums[mid]
                return find(l,mid)
            else:
                return find(mid+1,r) # don't matter where you add the +1 as long as not same as prev
        return find(0,len(nums)-1)

            

        

