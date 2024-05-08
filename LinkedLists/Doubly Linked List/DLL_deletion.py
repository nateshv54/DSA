class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
        self.prev=None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
        self.length=0

    def add_node_pos(self,data,pos):
        newnode=Node(data)
        if pos<0 or pos>self.length:
            print("Invalid Position")
            return
        if pos==0:
            if self.head is None:
                self.head=newnode
            if self.tail is None:
                self.tail=newnode
            else:
                self.head.prev=newnode

        
        else:
            current=self.head
            for _ in range(pos-1):
                current=current.next
            newnode.prev=current
            newnode.next=current.next
            if current.next is not None:
                current.next.prev=newnode
            else:
                self.tail=newnode
            current.next=newnode
        self.length+=1

    def delete_pos(self,pos):
        if pos<0 and pos>= self.length:
            print("Invalid Position")
            return
        if pos==0:
            if self.head.next is None:
                self.head=self.tail=None
            else:
                self.head=self.head.next
                self.head.prev=None
        else:
            current=self.head
            for _ in range(pos-1):
                current=current.next
            if current.next ==self.tail:
                self.tail=current
                current.next=None
            else:
                current.next=current.next.next
                current.next.prev=current
    
    def beg_delete(self):
        if self.head is None:
            print("List is empty, nothing to delete")
            return
        if self.head.next is None:
            self.head=self.tail=None
        else:
            self.head=self.head.next
            self.head.prev=None

        self.length-=1

    def end_delete(self):
        if self.head is None:
            print("List is empty, nothing to delete")
            return
        
        if self.head.next is None:
            self.head=self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None
        self.length-=1

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        Current=self.head
        while Current is not None:
            print(Current.data,end=" ")
            if Current.next is not None:
                print("<=>",end=" ")
            Current=Current.next
        print()
    def __len__(self):
        return self.length


l=DoublyLinkedList()
l.add_node_pos(1,0)
l.add_node_pos(2,1)
l.add_node_pos(3,2)
l.add_node_pos(4,len(l)//2)
l.display()
l.delete_pos(1)
l.beg_delete()
l.end_delete()
l.display()
