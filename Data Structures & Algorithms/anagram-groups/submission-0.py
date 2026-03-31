class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0]*26
             # what if no c
            for c in s:
                num = ord(c)-ord('a')
                count[num] += 1
            key = tuple(count)
            res[key].append(s)
        return list(res.values()) 
        
                
