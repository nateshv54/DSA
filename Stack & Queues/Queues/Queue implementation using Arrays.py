class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("enqueue to full queue")
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def front_item(self):
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.queue[self.front]

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def queue_size(self):
        return self.size

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            current = self.front
            while current != self.rear:
                print(self.queue[current], end=" ")
                current = (current + 1) % self.capacity
            print(self.queue[self.rear])

# Example usage
queue = Queue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue size:", queue.queue_size())
print("Front item:", queue.front_item())

print("\nElements of Queue are: ")
queue.display()

while not queue.is_empty():
    print("Dequeued:", queue.dequeue())
