class MinStack:

    def __init__(self):
        self.in_stack, self.out_stack = [], []
        

    def push(self, val: int) -> None:
        self.in_stack.append(val)
        val = min(val, self.out_stack[-1] if self.out_stack else val)
        self.out_stack.append(val)

    def pop(self) -> None:
        self.in_stack.pop()
        self.out_stack.pop()
        

    def top(self) -> int:
        return self.in_stack[-1]
        

    def getMin(self) -> int:
        return self.out_stack[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()