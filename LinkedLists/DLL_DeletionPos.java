package LinkedLists;

import LinkedLists.LinkedList.Node;

public class DLL_DeletionPos {
	public class Node{
		int data;
		Node next,prev;
		public Node(int data) {
			this.next=null;
			this.data=data;
			this.prev=null;
			}
	}
	public Node head=null;
	public Node tail=null;
	
	public void addnodepos(int data,int pos) {
		Node newnode=new Node(data);
		if(pos<0) {
			System.out.print("Invalid position "+pos);
		}
		if(pos==0) {
			newnode.next=head;
			if(head!=null) {
				head.prev=newnode;
			}
			head=newnode;
			if(tail==null) {
				tail=newnode;
			}
			return;
		}
		Node current=head;
		int currpos=0;
		while(current!=null && currpos<pos-1) {
			current=current.next;
			currpos++;
		}
		if(current==null) {
			System.out.print("Invalid position");
			return;
		}
		newnode.next=current.next;
		newnode.prev=current;
		if(current.next!=null) {
			current.next.prev=newnode;
		}
		else {
			tail=newnode;
		}
		current.next=newnode;
	}
	public void deletePos(int pos) {
		if(pos<0) {
			System.out.println("Invalid position");
			return;
		}
		if(pos==0) {
			if(head==null) {
				System.out.println("List is empty");
				return;
			}
			head=head.next;
			
			}
		Node current=head;
		int currpos=0;
		while(currpos<pos-1 && current!=null) {
			current=current.next;
			currpos++;
		}
		if(current==null) {
			System.out.print("Out of bonds" );
			return;
		}
		if(current.next!=null) {
			//setting next element previous address to 
			//present element address
			current.next.prev=current.prev;
		}
		else {
			//If last node is deleted
			tail=current.prev;
		}
		current.prev.next=current.next;
	}
	public void display() {
        Node current = head;
        if (head == null) {
            System.out.println("List is empty");
            return;
        }
        System.out.println("Nodes of doubly linked list: ");
        while (current != null) {
            System.out.print(current.data);
            if(current.next!=null) {
            	System.out.print(" => ");
            }
            current = current.next;
        }
        System.out.println();
    }
	static public void main(String args[]) {
		DLL_DeletionPos l=new DLL_DeletionPos();
		l.addnodepos(2, 0);
		l.addnodepos(3, 1);
		l.addnodepos(4, 2);
		l.addnodepos(5, 3);
		l.display();
		l.deletePos(0);
		l.display();
	}
}
