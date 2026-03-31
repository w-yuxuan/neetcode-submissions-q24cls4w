class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l <r: ##########
            mid = (l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
                
            else:r=mid 
        
        mid = l 
        l=0
        r=len(nums)-1
        
        if target<nums[mid] or target > nums[mid-1]:
            return -1
        elif nums[mid]<=target<=nums[r]:
            l=mid
        else: r = mid
        while l<r:
            mid = (r+l)//2
            if target==nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid-1
            else: l = mid+1        
        
        return l if nums[l] == target else -1




