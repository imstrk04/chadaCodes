class MinStack:

    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        current_top = self.main_stack[-1]
        self.main_stack.pop()

        if current_top == self.min_stack[-1]:
            self.min_stack.pop()


    def top(self) -> int:
        if not self.main_stack:
            return None
        return self.main_stack[-1]

    def getMin(self) -> int:
        if len(self.min_stack) == 0:
            return None  
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()