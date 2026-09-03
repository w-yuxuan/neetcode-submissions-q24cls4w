class Solution:
    def checkValidString(self, s: str) -> bool:
        # at least O(N)time ,1 memory, no i need n memory to store

        q=deque()
        forgive = 0
        # for in s:
        #     if i=="(":
        #         l+=1
        #     elif i ==")":
        #         r+=1
        #     else: forgive+=1
        # if forgive < abs(l-r):
        #     return False
        f = deque()
        for i in range(len(s)):
            if s[i]=="(":
                q.append((i))
            elif s[i] == "*":
                forgive+=1
                f.append(i)
            else:
                if q:
                    q.pop()
                else: # if there's not enough (, too much ), any  in front can save
                    if forgive <= 0:
                        return False
                    forgive -=1
                    f.popleft() # any one would work but we prioritize popping left ones to save the right ones for cases when we have too much (

        # if there's too much (
        while q and f:
            if q[-1] < f[-1]:
                f.pop()
                q.pop()
            else:
                return False

        return  len(q) == 0