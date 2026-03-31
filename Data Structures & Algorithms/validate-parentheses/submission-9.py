class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')',
            '[':']',
            '{':'}'}
        q = deque()

        for i,st in enumerate(s):
            if st in dic:
                q.append(st)
                continue
            else: #assume all inputs are some bracket 
                if q: #2 ways to F for st == closing bracket: have a closing bracket that doesn't match previous, or not having anyopen brackets at all 
                    if dic[q[-1]] == st :
                        q.pop()
                    else: return False
                elif st not in dic:
                    return False
        if not q:
            return True  # anotherway to F: after the for loop is done with have unpaired brackets in the {}
        else:return False
            
                

        