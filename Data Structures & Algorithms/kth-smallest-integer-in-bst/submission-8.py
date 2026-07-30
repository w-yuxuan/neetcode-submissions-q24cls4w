class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        
        while True:
            # 1. Fast push down the left branch
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # 2. Process
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            
            # 3. Move right
            curr = curr.right