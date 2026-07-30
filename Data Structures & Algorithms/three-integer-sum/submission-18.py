class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # n log n
        n= len(nums)
        res = []
        # brute force, find all triplets: o(n^3)
        # two pointer: pick one as i, and find j k pairs, put jk at two ends to mimic a binary search
        for i in range(len(nums)):

            j , k = i+1, n-1
            while j < k:
                tot = nums[j]+ nums[k]
                
                if tot == -nums[i]:
                    if [nums[i],nums[j],nums[k]] not in res:
                        res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                elif tot > -nums[i]: 
                    k-=1
                else: j+=1
        return res
        

        # code binary search afte ths 