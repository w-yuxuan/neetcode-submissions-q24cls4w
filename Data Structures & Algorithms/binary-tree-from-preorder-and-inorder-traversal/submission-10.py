
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return 
        
        pivot = preorder[0]
        ind = inorder.index(pivot)

        left = self.buildTree(preorder[1:1+ind],inorder[:ind])
        right = self.buildTree(preorder[1+ind:],inorder[ind+1:])

        root = TreeNode()
        root.left = left
        root.right = right
        root.val = preorder[0]
        return root
        
        # why when it's [1] we return [1] but sometimes in the ex at the bottom of tree we return None?