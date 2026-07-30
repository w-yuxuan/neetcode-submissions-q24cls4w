class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums)-1
        n = nums
        if len(nums)==1:
            if nums[0]==target:
                return 0
            else: return -1
        
        
        while l<r:
            mid = (l+r)//2

            if target == n[mid]:
                return mid
            if n[mid]< n[r]:
                if n[mid] < target <=  n[r]:
                    l = mid+1
                else:
                    r = mid
            else:
                if n[l]<= target <= n[mid]:
                    r = mid
                else:
                    l = mid+1
        if n[l] ==target:
            return l
        return -1


            
