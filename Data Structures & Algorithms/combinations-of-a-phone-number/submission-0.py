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
        
        if not digits:
            return []
        res = []
        cur = []

        def dfs(i):
            if i>len(digits)-1:
                res.append("".join(cur.copy()))
                return
            
            for j in range(len(mem[digits[i]])):
                lett = mem[digits[i]][j]
                cur.append(lett)
                dfs(i+1)
                cur.pop()

        dfs(0)
        return res