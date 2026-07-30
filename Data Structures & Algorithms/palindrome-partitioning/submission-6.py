class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # decision at every letter is to include it in the current set of palindrome or to start a new palindrome 
        res,collect,cur = [],[],[s[0]]
        # if len(s)==1:return s

        def check(i):
            nonlocal res,collect,cur
            #store result in collect, add to res only if we make one to the end that only conatins palindromes
            # if i>=len(s) and palin(res[-1]): # in case the final string is a single letter and haven't been checked if it's a palin. But then still the and part is not necessary
            if i>=len(s):
                if palin(cur):
                    # res.append("".join(cur))
                    res.append(collect+["".join(cur)]) # this addds a list inisde res, not a string 
            # return res # if you want to use this to return to the top, you need to return all the check(i+1) below.
                # but here we are editing a global var res so we can just return res after all algo is done
                return
            # cur="".join(cur,s[i]) # can't do this bc then we can't pop the last letter
            cur.append(s[i])
            check(i+1)
            cur.pop()
            # else:cur = [] # shouldn't clear, else it destroys the previously store letters stored, while the next letter might make this a palindrome
            
            if palin(cur):
                #start a new string
                old_cur=list(cur)
                
                collect.append("".join(cur)) #join them since we know everything in cur makes a palindrome 
                # collect.append(cur)
                cur = [s[i]]
                check(i+1)
                collect.pop()
                cur = old_cur
                

        def palin(s):
            n = len(s)
            if len(s)==1:
                return True
            l,r = 0,n-1
            while l<r:
                if s[l]!=s[r]:
                    return False

                l+=1
                r-=1
            return True

        check(1)
        return res

        
        