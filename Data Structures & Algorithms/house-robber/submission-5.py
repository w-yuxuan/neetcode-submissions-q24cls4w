class Solution:
    def rob(self, nums: List[int]) -> int:
        one,two=0,0
        #[one,two,n,n+1]
        for n in range(len(nums)):
            temp = max(two,nums[n]+one)
            one = two
            two = temp
        return two