class MinStack:

    def __init__(self):
        self.stack=[]
        

    def push(self, val: int) -> None:
        return self.stack.append(val)
        
    def pop(self) -> None:
        return self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        self.min=self.stack[0]
        for i in range(1,len(self.stack)):
            if self.stack[i]<self.min:
                self.min=self.stack[i]
        return self.min