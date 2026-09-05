class Node:
    def __init__(self):
        # self.val = val
        self.d = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        dum = self.root
        for i in word:
            if i not in dum.d:
                dum.d[i] = Node()
            dum = dum.d[i]
        dum.end = True      

    def search(self, word: str) -> bool:
        dum = self.root
        for i in word:
            if i not in dum.d:
                return False
            dum = dum.d[i]
        return dum.end == True

    def startsWith(self, prefix: str) -> bool:
        dum = self.root
        for i in prefix:
            if i not in dum.d:
                return False
            dum = dum.d[i]
        return True
        