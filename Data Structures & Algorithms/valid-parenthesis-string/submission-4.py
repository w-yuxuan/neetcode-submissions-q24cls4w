from collections import deque

class Solution:
    def checkValidString(self, s: str) -> bool:
        q = deque()
        f = deque()
        forgive = 0

        for i in range(len(s)):
            if s[i] == "(":
                q.append(i)
            elif s[i] == "*":
                forgive += 1
                f.append(i)
            else:
                if q:
                    q.pop()
                else:
                    if forgive <= 0:
                        return False
                    forgive -= 1
                    f.popleft()  # Keeps f in sync when a '*' handles a ')'

        # Run ONCE after the entire string is processed:
        # A remaining '(' can only be closed by a '*' that appears AFTER it (q[-1] < f[-1])
        while q and f:
            if q[-1] < f[-1]:
                q.pop()
                f.pop()
            else:
                return False  # '(' is after '*', impossible to close

        return len(q) == 0