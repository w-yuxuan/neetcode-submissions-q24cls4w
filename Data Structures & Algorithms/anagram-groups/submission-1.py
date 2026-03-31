class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s: #update count embedding, what if non?
                num = ord(c)-ord('a')
                count[num] +=1
            key = tuple(count)
            res[key].append(s)
        return list(res.values())



                
