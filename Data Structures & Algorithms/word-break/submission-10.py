class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[-1] = True

        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                d = len(w)
                if i+d > len(s):
                    continue
                # if d //can check len match
                # if s[i+1-d:i+1] == w and dp[i+1]:
                if s[i:i+d] == w and dp[i+d]:
                    dp[i]=True
                    break 
        return dp[0]
                

            