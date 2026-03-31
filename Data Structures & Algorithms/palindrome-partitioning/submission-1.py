#plan 2: keep spliting into two and if a config is a palindrome, add to that 
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        cur = []
        res = []
        j=0
        i=1
        if len(s)==1:
            return [[s]]
        
        def check(st): # check palindrome
            i = 0 
            j = len(st) - 1
            while 0<=i<j<=len(st)-1:
                if st[i] != st [j]:
                    return False
                i+=1
                j-=1
            return True 

        def find(j):
            if j > len(s)-1:
                res.append(cur.copy())
                return
            for i in range(j,len(s)):
                part = s[j:i+1]
                if check(part):
                    cur.append(part)
                    find(i+1) 
                    cur.pop()
        find(0)
        return res


