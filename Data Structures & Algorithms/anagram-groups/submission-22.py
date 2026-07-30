class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # count the letter occurance for each word 
        store = defaultdict(list)

        mem = [[0]*26 for i in range(len(strs))] 
        for i, word in enumerate(strs):
            for j,lett in enumerate(word):
                mem[i][ord(lett)-ord('a')]+=1
            store[tuple(mem[i])].append(word)
        return list(store.values())

        

        # i need to group all the words with the same letter frequencies

