class MinStack:

    def __init__(self):
        self.lowestIndices = []
        self.lowestIndex = 0
        self.stack = []
        self.stackIndex = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.stackIndex += 1
        # Initialise lowest value
        if len(self.lowestIndices) == 0:
            self.lowestIndices.append(val)
            self.lowestIndex += 1
        elif val <= self.lowestIndices[self.lowestIndex - 1]:
            self.lowestIndices.append(val)
            self.lowestIndex += 1

    def pop(self) -> None:
        valuePopped = self.stack.pop()
        self.stackIndex -= 1
        if valuePopped == self.lowestIndices[self.lowestIndex - 1]:
            self.lowestIndices.pop()
            self.lowestIndex -= 1

    def top(self) -> int:
        return self.stack[self.stackIndex - 1]

    def getMin(self) -> int:
        return self.lowestIndices[self.lowestIndex - 1]
