class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        dictt = {'(':')','[':']','{':'}'}

        for i,st in enumerate(s):
            if st in dictt:
                q.append(st)
                continue
            else: # need to check if only parenthesis related char are in the s
                if q:
                    if st == dictt[q[-1]]:
                        q.pop()
                    else: return False
                else:
                    return False
        return True if not q else False
        

            
