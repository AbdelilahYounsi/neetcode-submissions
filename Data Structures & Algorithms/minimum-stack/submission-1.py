class MinStack:

    def __init__(self):
        self.stack = []
        self.min_elt_list = [float('inf')]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val<self.min_elt_list[-1]:
            self.min_elt_list.append(val)
        else:
            min_elt = self.min_elt_list[-1]
            self.min_elt_list.append(min_elt)

    def pop(self) -> None:
        self.stack.pop()
        self.min_elt_list.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_elt_list[-1]
        
