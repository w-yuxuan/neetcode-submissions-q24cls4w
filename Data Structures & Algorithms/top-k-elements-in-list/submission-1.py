class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hash count each number's (frequency, string)
        # sort the values, yet frequencies won't be unique as keys 
        # don't do a hash: do a table is enough
        #max_counts = [0]*k

        # build the vocab then turn value to list, find the max in list, find index, turn the keys into list as well, repeat
        vocab = {}
        for n in nums:
            vocab[n] = vocab.get(n,0) + 1
        
        l_val = list(vocab.values())
        l_key = list(vocab.keys())
        
        #use heap
        #heap = heapq.heapify(l_val)
        #heap.maxheap()

        candidates = heapq.nlargest(k,l_val)
        res = []
        for i in candidates:
            pos = l_val.index(i)
            l_val.remove(i)
            res.append(l_key[pos])
            del l_key[pos]
        
        return res