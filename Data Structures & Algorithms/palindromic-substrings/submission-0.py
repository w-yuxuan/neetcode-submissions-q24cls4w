class Solution:
    def countSubstrings(self, s: str) -> int:
        leng = 0
        start = 0
        count=0
        #count1,count2 =0,0
        for i in range(len(s)):
            l,r = i,i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                if r+1-l > leng:
                    leng = r+1-l
                    start = l
                l-=1
                r+=1

            
            l,r = i,i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count+=1
                if r+1-l > leng:
                    leng = r+1-l
                    start = l
                l-=1
                r+=1
            
        return count #max(count1,count2)



        