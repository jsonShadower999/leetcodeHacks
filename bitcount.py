# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0]*(n+1)
        sub=1
        for i in range(1,n+1):
             if sub*2 ==i:
                sub=i
            dp[i]=dp[i-sub]+1
        return dp        
       
