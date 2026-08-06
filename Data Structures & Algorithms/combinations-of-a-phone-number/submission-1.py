class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mem = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        cur,res = '',[]
        if not digits:
            return []
        # for d in digits:
        def dfs(i,cur):
            if i >= len(digits):
                res.append(cur)
                return
            for l in mem[digits[i]]:
                # new = ''.join(cur,l)
                new = cur+l
                dfs(i+1,new)
        dfs(0,'')
        return res