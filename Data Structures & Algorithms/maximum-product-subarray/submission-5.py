class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize maxv to the first element (or a very small number)
        maxv = nums[0]
        
        # Pass 1: Forward (Left to Right)
        cur = 1
        for val in nums:
            cur *= val
            maxv = max(maxv, cur)
            # If we hit a 0, it "kills" the product chain.
            # Reset cur to 1 to start a fresh subarray product.
            if cur == 0:
                cur = 1
        
        # Pass 2: Backward (Right to Left)
        # We need this because if we have a single negative number (e.g., [1, 2, -5, 3, 4]),
        # the forward pass might carry that negative sign to the end.
        # The backward pass ensures we calculate the product of the valid segment on the other side.
        cur = 1
        for i in range(len(nums) - 1, -1, -1):
            cur *= nums[i]
            maxv = max(maxv, cur)
            if cur == 0:
                cur = 1
                
        return maxv