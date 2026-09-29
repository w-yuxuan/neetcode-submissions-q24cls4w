# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def dfs(node):
            if not node:
                return 0
            
            # 1. Check if result is already computed
            if node in memo:
                return memo[node]
            
            # Option 1: Rob this node + all 4 grandchildren
            rob_this = node.val
            if node.left:
                rob_this += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                rob_this += dfs(node.right.left) + dfs(node.right.right)
            
            # Option 2: Skip this node, rob left and right children
            skip_this = dfs(node.left) + dfs(node.right)
            
            # 2. Store the result in the memo hash map
            memo[node] = max(rob_this, skip_this)
            
            return memo[node]

        return dfs(root)