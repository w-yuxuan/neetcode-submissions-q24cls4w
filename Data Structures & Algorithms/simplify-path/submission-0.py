class Solution:
    def simplifyPath(self, path: str) -> str:
        q = deque()
        seg = path.split('/')
        res = []
        for s in seg:
            if s =='..':
                if res:
                    res.pop()
            elif s=='.' or s=='': # or '' when you have multiple //: do nothing
                continue
            else:
                res.append(s)
        return '/'+'/'.join(res)
