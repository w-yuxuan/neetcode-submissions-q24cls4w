class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # i can either choose to enclose one of the existing () or create one on the side
        # yet there are many () you can wrap another layer on, so that's not a 2-choice q

        #hint: i previously thoguth i need to do a stack method like the prev q, popping when we from a valid parentheiss
        # but here we actually control not just how we pop but what we add to the string each time as well, so we can just 
        # add ( then ), and count the number of ) and ( 
        res = []
        cur = []

        op = 0
        cl = 0

        def find(i,cl,op):
            # base: 
            if cl > op or cl > n or op > n:
                return
            if  i ==2*n:
                res.append(''.join(cur))
                #res.append(cur.copy())
                return 
            cur.append('(')
            find(i+1,cl,op+1)
            cur.pop()

            cur.append(')')
            find(i+1,cl+1,op)
            cur.pop()
        find(0,0,0)
        return res

            # convert lst of strings to list
            
            