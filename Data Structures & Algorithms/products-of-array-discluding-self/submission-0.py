class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # instead of prefix sum: we do prefix product.
        # we can do one from the left and one from the right, multiply them 
        p = 1
        left = []
        res= []
        right = deque()
        for i,n in enumerate(nums):
            p = p*n
            left.append(p)
        p=1
        for i,n in enumerate(nums[::-1]):
            p = p*n
            right.appendleft(p)

        for i,n in enumerate(nums):
            if i==0:
                res.append(right[i+1])
            elif i==len(nums)-1:
                res.append(left[i-1])
            else:res.append(left[i-1]*right[i+1])

        return res
