class MinStack:

    def __init__(self):
        self.s = []
        self.minStack = []

    def push(self, value: int) -> None:
        self.s.append(value)
        if not self.minStack:
            self.minStack.append(value)
        else:
            self.minStack.append(min(self.minStack[-1], value))

    def pop(self) -> None:
        if not self.s:
            return
        self.s.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()