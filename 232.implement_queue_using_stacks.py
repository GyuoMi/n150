class MyQueue:

    def __init__(self):
        self.in_stack = [] 
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)
        

    def pop(self) -> int:
        # we can write a simple single stack and just do pop(0)
        # but that would be O(N) since each element needs to be shifted 1 pos left
        # if the out stack is empty, transfer elements from the in stack
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        # out stack now has the oldest item on the top
        return self.out_stack.pop()
        

    def peek(self) -> int:
        # same logic as pop but no removal
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]
        

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()