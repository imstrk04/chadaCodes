class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        prefixMax = [-1] * len(height)
        suffixMax = [-1] * len(height)

        prefixMax[0] = height[0]
        suffixMax[n - 1] = height[-1]

        for i in range(1,len(height)):
            prefixMax[i] = max(prefixMax[i-1], height[i])
        
        for i in range(len(height) - 2, -1, -1):
            suffixMax[i] = max(suffixMax[i+1],height[i])
        
        total = 0
        for i in range(n):
            if height[i] < prefixMax[i] and height[i] < suffixMax[i]:
                total += min(prefixMax[i], suffixMax[i]) - height[i]
        
        return total