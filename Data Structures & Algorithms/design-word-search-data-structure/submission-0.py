class node:
    def __init__(self):
        self.d = {}
        self.end = False
        self.free = 0
class WordDictionary:

    def __init__(self):
        self.root = node()
        

    def addWord(self, word: str) -> None:
        dum = self.root
        for i in word:
            if i not in dum.d:
                dum.d[i] = node()
            dum = dum.d[i]
        dum.end = True

    def dfs(self,word,dum):
        for i in range(len(word)):
            if word[i] =='.':
                for j in dum.d.values(): # continue searching from all oth possibilities j
                    dum = j
                    if self.dfs(word[i+1:],dum):
                        return True
                return False
            else:
                if word[i] not in dum.d:
                    return False
                dum = dum.d[word[i]] # 6. Actually advance 'dum' to the next node
        return dum.end==True        

    def search(self, word: str) -> bool:
        dum = self.root
        return self.dfs(word,dum)
        
        
