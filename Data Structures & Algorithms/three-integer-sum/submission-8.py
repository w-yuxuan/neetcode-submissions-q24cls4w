class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #1 bruthe force: n^2 two numb configs, calculate the third, verify if it's there: n^3
        #2 sort and binary search for the thrird?
        #3 sort isn't helping since knowing the two's relative magnitiude isn't helpful: it still dep on the thrid's existance?
            ## if i don't sort: check all n^2 combinations, brute. if i sort: only n log n
            #and find that the third must be larger than the largest, i don't further check
        #plan: two pointer after sort, if ij same sign: return 0, else search everything in btw
        #next iter: only move one side is enough? yes, bc the third number can be anything in between
        #see hint4. avoid duplicates by jumping twice if 

        nums.sort()
        res = []
        
        for i in range(len(nums)-1):
            if nums[i]>0: #jk are larger and can't get 0
                break

            j,k=i+1,len(nums)-1
            if i>0 and nums[i-1]==nums[i]:
                continue                
            while j<k:
                if nums[i]==-nums[j]-nums[k]:
                    res.append([nums[i],nums[j],nums[k]])
                    #prune if j and k values have duplicates
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and  nums[k]==nums[k+1]: k-=1

                # if both j and k side has duplicate, skip both since they give a dup result
                # if one side duplicates, skip that side
                # if no side dpulicates, skip any side 
                elif nums[i]> -nums[j]-nums[k]:
                    k-=1
                else: j+=1

        return res

        
        


