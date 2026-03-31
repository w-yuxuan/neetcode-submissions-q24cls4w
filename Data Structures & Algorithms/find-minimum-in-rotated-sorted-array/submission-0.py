class Solution:
    def findMin(self, nums: List[int]) -> int:
        #key is to find the rotation point: the index it goes from the largest number to the smallest number 
        # ofc it can only rotate n times since n> that is repeating 
        
        l = 0
        r = len(nums)-1
        def find(l,r):
            mid = (l+r)//2

            if l == r:
                return nums[l]
            if nums[r]< nums[mid]:
                return find(mid+1,r)
            else: return find(l,mid)
        return find(l,r)

            

        

