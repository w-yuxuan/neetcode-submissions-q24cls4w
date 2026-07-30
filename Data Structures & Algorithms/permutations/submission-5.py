class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        l = 0
        res = deque([[]])

        for i in nums:
            for _ in range(len(res)):
                p = res.popleft()
                for j in range(l+1):
                    new = p.copy()
                    new.insert(j,i)
                    res.append(new)

            l+=1
        return list(res)
            
