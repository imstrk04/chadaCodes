class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        abs1 = abs(x - z)
        abs2 = abs(y - z)

        if abs1 > abs2:
            return 2
        elif abs1 < abs2:
            return 1
        else:
            return 0