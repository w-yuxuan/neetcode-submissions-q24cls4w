# revisit's fix
# 
# 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math

class Solution:
        def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

            def build(preorder,inorder):
                if not preorder or not inorder:
                #    res.append(None)
                    return #else preorder[0] causes error when empty
                root = TreeNode(preorder[0])
               # res.append(root)
                s=inorder.index(preorder[0])

                root.left = build(preorder[1:s+1] ,inorder[:s])
                root.right = build(preorder[s+1:],inorder[s+1:])
                # only append the root each time, else parts of left will be repeatedly written

                #build(preorder[1:s+1] ,inorder[:s])
                #build(preorder[s+1:],inorder[s+1:])
                #res.append(left)
                #res.append(right)
                return root
            
            return build(preorder,inorder)