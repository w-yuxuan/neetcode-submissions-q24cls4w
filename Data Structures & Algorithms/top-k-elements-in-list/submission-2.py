class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        vocab = {}

        for n in nums:
            vocab[n] = vocab.get(n,0)+1

        for n,c in vocab.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq)-1,0,-1): #len
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res