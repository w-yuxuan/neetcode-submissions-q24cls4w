class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # list of list type dict
        vocab = defaultdict(list)
        for s in strs: #embedd
            emb = [0]*26
            for c in s:
                num = ord(c)-ord('a')
                emb[num]+=1
            key = tuple(emb)
            vocab[key].append(s)
        return list(vocab.values())
            
                