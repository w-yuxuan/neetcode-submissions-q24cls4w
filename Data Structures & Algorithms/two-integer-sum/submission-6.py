class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for j,i in enumerate(nums):

            #dic.update({i,nums.index(i)})

            dic[i] = j
        for j,i in enumerate(nums):
            #if i <= target:
                #find = target-nums
                find = target -i

                if find in dic and dic[find] !=j:
                    res = [j,dic[find]]
                #if dic[i].val != None:
                    return res
                    