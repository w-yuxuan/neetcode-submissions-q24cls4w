# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:
        def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            #if preorder == None or inorder == None:why? see below
            if not preorder  or not inorder:
                return None

            root = TreeNode(preorder[0])
            mid = inorder.index(preorder[0])
            #you don't have to create a hash to find index of a number in an array
            root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
            root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])

            return root