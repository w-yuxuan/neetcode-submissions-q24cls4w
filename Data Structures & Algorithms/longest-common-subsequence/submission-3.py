class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # build cache
        mem = [[0]*(len(text2)+1) for i in range(len(text1)+1) ]
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    mem[i][j] = mem[i-1][j-1]+1
                else:
                    mem[i][j] = max(mem[i][j-1], mem[i-1][j])
        return mem[len(text1)][len(text2)]


        
            
            
