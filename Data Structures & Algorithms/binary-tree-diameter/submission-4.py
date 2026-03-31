# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        m = 0
        def find(node):
            nonlocal m
            if node.left and node.right:
                m = max(m,find(node.left)+1+find(node.right)+1)
                return max(find(node.left),find(node.right)) +1
            elif node.left:
                return find(node.left)+1
            elif node.right:
                return find(node.right)+1
            else: return 0
        if root:
            return find(root) if find(root)>m else m
        else: return 0 # if left and right side same len and l+r is longer than l+parent