class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL_Insertion:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        current = self.head
        length = 0
        while current is not None:
            length += 1
            current = current.next
        return length

    def insert_at_pos(self, data, pos):
        new_node = Node(data)
        if pos < 0 or pos > len(self):
            print("Invalid position")
            return
        if pos == 0:
            new_node.next = self.head
            if self.head is not None:
                self.head.prev = new_node
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
        else:
            current = self.head
            for _ in range(pos - 1):
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            if current.next is not None:
                current.next.prev = new_node
            else:
                self.tail = new_node
            current.next = new_node

    def insert_at_end(self, data, length):
        self.insert_at_pos(data, length)

    def display(self):
        current = self.head
        if self.head is None:
            print("List is empty")
            return
        print("Nodes of doubly linked list:")
        while current is not None:
            print(current.data, end="")
            if current.next is not None:
                print(" => ", end="")
            current = current.next
        print()

if __name__ == "__main__":
    l = DLL_Insertion()
    l.insert_at_pos(2, 0)
    l.insert_at_pos(3, 1)
    l.insert_at_pos(4, 2)
    l.insert_at_pos(5, 3)
    l.insert_at_end("M", len(l)//2)
    l.display()
'''
Nodes of doubly linked list:
2 => 3 => M => 4 => 5
'''