package LinkedLists;

public class DLL_Insertion {
	class Node{
		int data;
		Node prev,next;
		public Node(int data) {
			this.data=data;
			this.prev=null;
			this.next=null;
		}
	}
	public Node head=null;
	public Node tail=null;
	public void inseratpos(int data,int pos) {
		Node newnode=new Node(data);
		if(pos<0) {
			System.out.print("Invalid position");
			return;
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
		while(currpos<pos-1 && current!=null) {
			current=current.next;
			currpos++;
		}
		if(current==null) {
			System.out.print("Invalid position "+pos);
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
	public static void main(String[] args) {
        DLL_Insertion l = new DLL_Insertion();
        l.inseratpos(2, 0);
        l.inseratpos(3, 1);
        l.inseratpos(4, 2);
        l.inseratpos(5, 3);
        l.display();
    }

}
