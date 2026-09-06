class Node:
    def __init__(self):
        self.end = False
        self.d = {}

class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        dum = self.root
        for i in word:
            if i not in dum.d:
                dum.d[i]=Node()
            dum = dum.d[i] 
        dum.end = True

    def search(self, word: str) -> bool:
        def dfs(word,dum):
            for i in range(len(word)):
                if word[i]=='.':
                    for j in dum.d.values():
                        if dfs(word[i+1:],j):
                            return True
                    return False
                else:
                    if word[i] in dum.d:
                        dum = dum.d[word[i]]
                    else:
                        return False
            return dum.end==True
        return dfs(word,self.root)



        


        
