class MinStack:

    def __init__(self):
        self.stack = []
        self.floor = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.floor:
            self.floor.append(min(val,self.floor[-1]))
        else:
            self.floor.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.floor.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.floor[-1]
        
