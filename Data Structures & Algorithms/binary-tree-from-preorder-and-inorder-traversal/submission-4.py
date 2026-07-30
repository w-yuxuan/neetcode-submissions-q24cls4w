# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        res = []
        
        def find(preorder,inorder):
            
            # cur = []
            if not preorder:
                return None
            # if len(preorder)=1:
            #     return preorder

            # for i in preorder:
           
            # res.append(preorder[0])
            root = TreeNode(preorder[0])
            
            index = inorder.index(preorder[0])
            root.left = find(preorder[1:1+index],inorder[0:index])
            root.right = find(preorder[1+index:],inorder[index+1:])
            # res.append(left,right)
            return root
        
        return find(preorder,inorder)