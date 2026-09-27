class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        l = r = 0
        far = 0 
        
        q = deque()
        q.append(0)
        while q:
            for _ in range(len(q)):
                j = q.popleft()
                for i in range(j+minJump,min(maxJump+j,n-1)+1):
                    if s[i]=='1' or i <= far:
                        continue
                    far = max(far,i)
                    q.append(i)
                    
        return far >= n-1

            