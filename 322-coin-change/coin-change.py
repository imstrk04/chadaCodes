class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def f(ind, target):
            if ind == 0:
                return target // coins[0] if target % coins[0] == 0 else float('inf')

            notTake = 0 + f(ind - 1, target)
            take = float('inf')
            # i can only take if the coins[i] lesser than my target
            if coins[ind] <= target:
                take = 1 + f(ind, target - coins[ind])
             
            return min(take, notTake)
        
        n = len(coins)
        ans = f(n - 1, amount)  
        return ans if ans != float('inf') else -1