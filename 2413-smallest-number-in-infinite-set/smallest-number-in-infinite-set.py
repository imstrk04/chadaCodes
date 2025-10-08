class SmallestInfiniteSet:

    def __init__(self):
        self.nums = list(i+1 for i in range(1001))
        self.set = set(list(i+1 for i in range(1001)))
        heapq.heapify(self.nums)
    def popSmallest(self) -> int:
        num = heapq.heappop(self.nums)
        self.set.remove(num)
        return num

    def addBack(self, num: int) -> None:
        if num not in self.set:
            self.set.add(num)
            heapq.heappush(self.nums, num)



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)