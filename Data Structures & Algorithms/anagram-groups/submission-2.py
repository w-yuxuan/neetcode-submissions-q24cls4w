class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sorteds = ''.join(sorted(s))
            key = tuple(sorteds)
            res[key].append(s)
        return list(res.values())



                
