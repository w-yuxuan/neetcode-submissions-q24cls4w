class tnode:
    def __init__(self):
        self.end = False
        self.child = {}


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = tnode()
        n = len(s)
        # build Trie
        for word in dictionary:
            cur = root
            leng = len(word)
            for lett in word:
                if lett not in cur.child:
                    new = tnode()
                    cur.child[lett]= new
                    cur = new
                else:
                    cur = cur.child[lett]
            cur.end = True
        mem = {}
        # use trie
        def dfs(i):
            if i in mem:
                return mem[i]
            if i>n-1:
                return 0
            res = 1+dfs(i+1)
            cumulate_cost = 0
            cur2 = root # cur2 actually moves 
            for j in range(i,n):
                lett = s[j]
                cumulate_cost+=1
                if lett in cur2.child:
                    cur2 = cur2.child[lett]
                    if cur2.end: # actual word is longer than s' sequence, word not in trie,  need to go back
                        res = min(res,dfs(j+1))
                else:
                    break # go back to the original node and start searching from one letter after
            mem[i]=res
            return res
        return dfs(0)


            


        

                    


            
        