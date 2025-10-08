class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        leftSum = 0
        for i in range(k):
            leftSum += cardPoints[i]
        
        rightIndex = len(cardPoints) - 1
        rightSum = 0
        maxi = leftSum
        for i in range(k-1, -1, -1):
            leftSum = leftSum - cardPoints[i]
            rightSum = rightSum + cardPoints[rightIndex]
            rightIndex -= 1
            maxi = max(leftSum + rightSum, maxi)
        
        return maxi