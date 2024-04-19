class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL_Del_Pos:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0  # Keep track of the length of the linked list

    def add_new_node_pos(self, data, pos):
        new_node = Node(data)
        if pos < 0 or pos > self.length:  # Updated condition to check if pos is valid
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

    def delete_pos(self, pos):
        if pos < 0 or pos >= self.length:
            print("Invalid index")
            return
        if pos == 0:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
        else:
            current = self.head
            for _ in range(pos - 1):
                current = current.next
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next
        self.length -= 1

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        print("Nodes of Linkedlist are")
        while current is not None:
            print(current.data, end="")
            if current.next is not None:
                print(" => ", end="")
            current = current.next
        print()

    # Implementing the __len__ method to return the length of the linked list
    def __len__(self):
        return self.length

if __name__ == "__main__":
    l = SLL_Del_Pos()
    l.add_new_node_pos(1, 0)
    l.add_new_node_pos(2, 1)
    l.add_new_node_pos(3, 2)
    l.add_new_node_pos(4, 3)
    l.display()
    l.delete_pos(1)
    l.add_new_node_pos(2,1)
    l.add_new_node_pos('M', len(l)//2)
    l.display()
    l.delete_pos(len(l)//2)
    l.display()
'''
Nodes of Linkedlist are
1 => 2 => 3 => 4
Nodes of Linkedlist are
1 => 2 => M => 3 => 4'''