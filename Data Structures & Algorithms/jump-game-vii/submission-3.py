class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        far = 0
        if n==1:
            return True
        q = deque([0])
        while q:
            i = q.popleft()
            for j in range(max(i+minJump,far+1),min(n-1,i+maxJump)+1):
                if s[j]=='1':
                    continue
                far = j
                q.append(j)
                if j >=n-1:
                    return True
        return False
                