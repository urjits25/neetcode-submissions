class MinStack:

    def __init__(self):
        self.stack = []
        self.mono_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mono_min:
            self.mono_min.append(val)
        else:
            self.mono_min.append(min(self.mono_min[-1], val) )

    def pop(self) -> None:
        self.mono_min.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mono_min[-1]
        
