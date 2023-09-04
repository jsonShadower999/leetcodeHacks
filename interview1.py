# n :are no of stones,
# you start first
# you n your friend can throw upto 3 stones
def canWinNim(n):
  if(n<=3):
    return True
    # Create a list to store the winning status for each number of stones
    dp = [False] * (n + 1)
    
    # You can always win when there are 1, 2, or 3 stones left
    dp[1] = dp[2] = dp[3] = True
    
    # Calculate the winning status for each number of stones from 4 to n
    for i in range(4, n + 1):
        dp[i] = not (dp[i - 1] and dp[i - 2] and dp[i - 3])
    
    return dp[n]

# Example usage:
n = 4
print(canWinNim(n))  # Output: False
