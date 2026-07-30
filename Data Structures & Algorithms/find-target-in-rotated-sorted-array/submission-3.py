class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        res = -1
        if len(nums)==1:
            if nums[0] == target:
                return 0
            else: return -1
        while l<r:
            mid = (l+r)//2 # lean left
            # if nums[mid] == target:
            #     return mid 
            # elif nums[mid] 
            if nums[mid] > nums[r]:
                l = mid+1
            else:
                r = mid
        s = nums[l:]+nums[:l]
        
        pivot = l
        l,r = 0, len(nums)-1
        
        while l<=r:
            mid = (l+r)//2
            if s[mid] == target:
                if mid + pivot <= len(nums)-1:
                    return mid + pivot
                else: return mid + pivot- len(nums)
            elif s[mid]<target:
                l=mid+1
            else:
                r = mid - 1

        return res
