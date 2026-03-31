class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def help(i,nums): #create all possible ways to insert i into nums
            if i == len(nums):
                return [[]] #base case with pointer one level out of bounds
            resPerms = [] # individual case answer

            perms = help(i+1,nums)
            for p in perms: #generate all possible combin
                for j in range(len(p)+1): #number of places to insert is len(combi)+1
                    pcopy=p.copy()
                    pcopy.insert(j,nums[i])
                    resPerms.append(pcopy)
            return resPerms
        
        return help(0,nums)
        