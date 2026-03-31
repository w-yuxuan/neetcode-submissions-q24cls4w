class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # key is to not have pointers that are out of bounds
        #for i in range(len(numbers)//2):

        #can't use i and -i index since can't det if they crossed over 
        #i=len(numbers)//2

        r = len(numbers)-1
        l = 0

        #while r > l and # not needed now your for loop ensures this
        while r > l:
            if numbers[r] + numbers[l] == target:
                return [l+1, r+1]
            elif numbers[r] + numbers[l] < target:
                l+=1 
            elif numbers[r] + numbers[l] > target:
                r-=1


