class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        f = [1]
        b = deque([1])
        res = []
        
        n= 0

        #teest len(nums)=2
        for i in range(1,len(nums)):
            f.append(nums[i-1]*f[i-1])
        for i in range(len(nums)-2,-1,-1):
            b.appendleft(nums[i+1]*b[n-1])
            n-=1
        for i in range(0,len(nums)):
            res.append(b[i]*f[i])
        return res

