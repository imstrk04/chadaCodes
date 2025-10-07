class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        @lru_cache(None)
        def f(i):
            if i > n:
                return float('inf')
            
            if i == n:
                return 0


            #take one step
            one = f(i + 1) + (costs[i] if i < n else 0) + (1)**2

            # take two steps
            two = f(i + 2) + (costs[i+1] if i + 1 < n else 0) + (2)**2

            # take three steps
            three = f(i + 3) + (costs[i+2] if i + 2 < n else 0) + (3)**2

            return min(one,two,three)
        
        return f(0)
