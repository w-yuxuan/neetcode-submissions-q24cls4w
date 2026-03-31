class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = set()
        nums.sort()

        for i,n in enumerate(nums):
            g = (-1)*n

            if i > len(nums)-3: #avoid assinging j,k out of bounds, stop at nums[-3]
                break

            j=i+1 #only scan to the right to avoid duplicates
            k=len(nums)-1

            while j<k :#and j>i and k>i
                if nums[j] + nums[k] == g:
                    check = tuple([nums[i],nums[j],nums[k]])
                    #if check not in s:
                    s.add(check)
                    #res.append([nums[i],nums[j],nums[k]])
                    j+=1
                
                elif nums[j] + nums[k] > g:
                    k -= 1

                elif nums[j] + nums[k] < g:
                    j += 1
        #return list([v] for v in s)
        return list(list(v) for v in s)