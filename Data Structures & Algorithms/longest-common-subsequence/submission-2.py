class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # build cache
        mem= [[0]*(len(text2)+1) for i in range(len(text1)+1)]
        
        for i in range(1,len(text1)+1): 
            for j in range(1,len(text2)+1):
        # def find(i,j):
                # if i>len(text1) or j > len(text2): 
                #     return # no need to return bc I have been editing mem 
                if text1[i-1] == text2[j-1]: # text[0] correspond to matrix [1]
                    mem[i][j] = 1+mem[i-1][j-1]  #find(i-1,j-1)  
                else:
                    mem[i][j] = max(mem[i-1][j], mem[i][j-1])
        return mem[len(text1)][len(text2)]
        
            
            
