class MinStack:

    def __init__(self):
        self.l=[]
        

    def push(self, val: int) -> None:
        mn=val if not self.l else min(self.l[-1][1],val)
        return self.l.append([val,mn])
        

    def pop(self) -> None:
        return self.l.pop()

    def top(self) -> int:
        return self.l[-1][0]

    def getMin(self) -> int:
        
        return self.l[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()