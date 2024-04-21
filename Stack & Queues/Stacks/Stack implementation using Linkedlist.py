class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return popped_value

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.value

    def is_empty(self):
        return self.size == 0

    def stack_size(self):
        return self.size
    
    def display(self):
        current = self.top
        while current:
            print(current.value)
            current = current.next


# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack size:", stack.stack_size())
print("Stack peek:", stack.peek())
print("Elemetns of stack")
stack.display()

while not stack.is_empty():
    print("Popped:", stack.pop())
