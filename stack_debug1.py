

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        print(self.items)
        return self.items == []

    def push(self, item):
        self.items.append(item)
        print("After push: ", self.items)

    def pop(self):
        print("Before pop: ", self.items)
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)

    def print_stack(self):
        print("Stack: ", self.items)


stack = Stack()
print("stack.push(1)")
stack.push(1)
print("stack.push(2)")
stack.push(2)
print("stack.push(5)")
stack.push(5)
print("")
stack.pop()
stack.print_stack()
stack.pop()
stack.print_stack()
stack.pop()
stack.print_stack()
