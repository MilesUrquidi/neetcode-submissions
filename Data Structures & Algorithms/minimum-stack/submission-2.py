class MinStack:

    def __init__(self):
        self.stack = []
        self.lowest = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.lowest:
            self.lowest.append(min(self.lowest[-1],val))
        else:
            self.lowest.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.lowest.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.lowest[-1]
        
