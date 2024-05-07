class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.prev=None
        self.next=None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head=None
        self.tail=None
        self.length=0
    
    def addnewnode(self,data,pos):
        newnode=Node(data)
        if pos<0 or pos>self.length:
            print("Invalid Position")
            return
        if pos==0:
            if self.head is not None:
                self.head.prev=newnode
            self.head=newnode
            if self.tail is None:
                self.tail=newnode
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
    
    def node_beg(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        else:
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
        
    def node_end(self,data):
        newnode=Node(data)
        if self.head is None:
            self.tail=newnode
            self.head=newnode
        else:
            self.tail.next=newnode
            newnode.prev=self.tail
            self.tail=newnode

    def display(self):
        current=self.head
        if self.head is None:
            print("LinkedList is empty: ")
            return
        print("Nodes of Doubly Linkedlist are: ")
        while current is not None:
            print(current.data,end=" ")
            if current.next is not None:
                print("<=>",end=" ")
            current=current.next
        print()     

    def __len__(self):
        return self.length
        


if __name__=="__main__":
    l=DoublyLinkedList()
    l.addnewnode(2,0)
    l.addnewnode(3,1)
    l.addnewnode(4,2)
    l.display()
    l.addnewnode("M",len(l))
    l.node_end("last")
    l.node_beg(1)
    l.display()
                 

'''
Nodes of Doubly Linkedlist are: 
2 <=> 3 <=> 4
Nodes of Doubly Linkedlist are:
1 <=> 2 <=> 3 <=> 4 <=> M <=> last
'''
