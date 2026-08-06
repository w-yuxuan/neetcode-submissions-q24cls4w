class TreeNode:
    def __init__(self,val=None,next = True):
        self.val = val
        self.next = next
        self.d = {}
class PrefixTree:

    def __init__(self):
        self.root = TreeNode()


    def insert(self, word: str) -> None:
        n = self.root
        for i in word:
            if i not in n.d:
                new = TreeNode()
                n.d[i] = new
            n = n.d[i]
            
        n.next = False
            # if i not in root

    def search(self, word: str) -> bool:
        n = self.root
        for i in word:
            if i not in n.d:
                return False
            n = n.d[i]
        return not n.next

    def startsWith(self, prefix: str) -> bool:
        n = self.root
        for i in prefix:
            if i not in n.d:
                return False
            n = n.d[i]
        return True
        