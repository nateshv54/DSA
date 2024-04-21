class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        dequeued_value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_value

    def front_item(self):
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.front.value

    def is_empty(self):
        return self.front is None

    def queue_size(self):
        current = self.front
        size = 0
        while current:
            size += 1
            current = current.next
        return size

    def display(self):
        current = self.front
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

# Example usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue size:", queue.queue_size())
print("Front item:", queue.front_item())

queue.display()

while not queue.is_empty():
    print("Dequeued:", queue.dequeue())
