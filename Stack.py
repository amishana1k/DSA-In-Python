class MyStack:

    def __init__(self):
        self.obj=deque()
        
    def push(self, x: int) -> None:
        self.obj.append(x)
        for _ in range(len(self.obj)-1):
            self.obj.append(self.obj.popleft())
        
    def pop(self) -> int:
        return self.obj.popleft()
        
    def top(self) -> int:
        return self.obj[0]
        
    def empty(self) -> bool:
        return len(self.obj)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

        
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
