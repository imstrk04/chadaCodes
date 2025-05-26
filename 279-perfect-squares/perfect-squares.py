class Solution:
    def numSquares(self, n: int) -> int:
        
        coins = [i * i for i in range(1, int(n**0.5) + 1)]

        amount = n

        dp = [float('inf')] * (n + 1)
        dp[0] = 0
    
        for amt in range(1, amount + 1):
            for coin in coins:
                if amt - coin >= 0:
                    dp[amt] = min(dp[amt], dp[amt - coin] + 1)

        
        return dp[amount]