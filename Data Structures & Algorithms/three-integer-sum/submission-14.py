class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i,j,k = 0,1,2
        res = []
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j = i+1
            k= len(nums)-1
            while j<k:
                goal = -nums[i]-nums[j]
                if nums[k] > goal:
                    k -=1
                elif nums[k] == goal:
                    res.append([nums[i],nums[j],nums[k]])
                    while j+1<=k and nums[j+1]==nums[j]:
                        j+=1
                    while j+1<=k and nums[k-1]==nums[k]:
                        k-=1
                    j+=1
                    k-=1          
                else: j+=1
        return res

                