class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        res = -1
        if len(nums)==1:
            if nums[0] == target:
                return 0
        while l<r:
            mid = (l+r)//2 # lean left
            # if nums[mid] == target:
            #     return mid 
            # elif nums[mid] 
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
        # s = nums[l:]+nums[:l]
        if nums[l]<=target<=nums[-1]:
            l,r = l, len(nums)-1
        elif nums[0] <= target <= nums[l-1]:
            l,r = 0, l-1
        else: return -1
        
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                l=mid+1
            else:
                r = mid - 1

        return res
