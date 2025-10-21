class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1 for _ in range(amount + 1)] for _ in range(n)]
        def f(ind, target):
            if ind == 0:
                if target % coins[0] == 0:
                    return target // coins[0]
                else:
                    return float('inf')
            
            if dp[ind][target] != -1:
                return dp[ind][target]

            notTake = f(ind - 1, target)
            take = float('inf')
            if target >= coins[ind]:
                take = 1+ f(ind, target - coins[ind]) # stay here till u can take the coin as many times as u can till the if condition fails
            
            dp[ind][target] = min(take, notTake)   
            return dp[ind][target]
        
        ans = f(n - 1, amount)
        return -1 if ans == float('inf') else ans
