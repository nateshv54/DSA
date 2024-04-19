class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0  # Initialize the length of the linked list to 0

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1  # Increment the length of the linked list

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        print("Nodes of the linked list:")
        while current is not None:
            print(current.data, end="")
            if current.next is not None:
                print(" => ", end="")
            current = current.next
        print()

    def add_node_at_pos(self, data, pos):
        new_node = Node(data)
        if pos < 0 or pos > self.length:
            print("Invalid Position")
            return
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
        else:
            current = self.head
            for _ in range(pos - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            if pos == self.length:
                self.tail = new_node
        self.length += 1

    def __len__(self):
        return self.length

if __name__ == "__main__":
    l = LinkedList()
    l.add_node(10)
    l.add_node(11)
    l.add_node(12)
    l.display()

    # Add a node with data 13 at position 1
    l.add_node_at_pos(13, 1)
    
    # Add a node with data 'k' at the middle position
    l.add_node_at_pos('k', len(l) // 2)
    
    l.display()

'''
Nodes of the linked list:
10 => 11 => 12
Nodes of the linked list:
10 => 13 => k => 11 => 12
'''