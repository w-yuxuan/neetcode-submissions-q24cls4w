class TreeNode:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr.children:
                curr.children[i] = TreeNode() # not 'i' but the var
                
            #if i == word[len(word)-1]: # don't need to check this, just do it after for ends
            #    curr.end == True 

            curr = curr.children[i]  # shift pointer to the next Treenode (and the only next treenode)         
            #curr = curr.children 
            #wrong to point self.root to  {} bc you stepped off the graph pattern:
            #in the for loop next step you call curr.children and you will have err
    
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i in word:
            if i not in curr.children:
                return False
            curr = curr.children[i]
        #return True
        return curr.end #you looped through the whole word, doesn't mean they agree. If there are less letters in word than og, then still false
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in prefix:
            if i not in curr.children:
                return False
            curr = curr.children[i]
        return True