package LinkedLists;

public class SLL_Del_Pos {
	public class Node{
		int data;
		Node next;
		public Node(int data) {
			this.data=data;
			this.next=null;
		}
	}
	public Node head=null;
	public Node tail=null;
	public void addnewnodePos(int data,int pos) {
		Node newnode=new Node(data);
		if(pos<0) {
			System.out.print("Invalid Position");
			return;
		}
		if(pos==0) {
			newnode.next=head;
			head=newnode;
			if(tail==null) {
				tail=newnode;
				return;     //return should be used to terminate infinite loop behavior
				
			}
		}
		Node current=head;
		int currpos=0;
		while(currpos<pos-1 && current!=null) {
			current=current.next;
			currpos++;
		}
		if(current==null) {
			System.out.print("Invalid position"+pos);
		}
		newnode.next=current.next;
		current.next=newnode;
		if(tail==null) {
			tail=newnode;
		}
		
	}
	public void deletePos(int pos) {
		if(head==null) {
			System.out.println("List is empty");
			return;
		}
		if(pos<0) {
			System.out.println("Invalid index");
			return;
		}
		if(pos==0) {
			if(head==tail) {
				head=tail=null;
			}
			else {
				//set head to next element
				
				head=head.next;
			}
			return;
		}
		Node current=head;
		int currpos=0;
		while(currpos<pos-1 && current!=null) {
			current=current.next;
			currpos++;
		}
		if(current==null ||current.next==null) {
			System.out.print("Invalid position "+pos);
			return;
		}
		if(current.next==tail) {
			tail=current;
		}
		//set current address to deleting element address
		
		current.next=current.next.next;
	}
	public void display() {
		if(head==null) {
			System.out.println("List is empty ");
			return;
		}
		Node current=head;
		System.out.println("Nodes of Linkedlist are");
		while(current!=null) {
			System.out.print(current.data);
			if(current.next!=null) {
				System.out.print(" => ");
			}
			current=current.next;
		}
		System.out.println();
	}
	static public void main(String args[]) {
		SLL_Del_Pos l=new SLL_Del_Pos();
		l.addnewnodePos(1, 0);
		l.addnewnodePos(2, 1);
		l.addnewnodePos(3, 2);
		l.addnewnodePos(4, 3);
		l.display();
		l.deletePos(1);
		l.display();
	}

}
/*

Nodes of Linkedlist are
1 => 2 => 3 => 4
Nodes of Linkedlist are
1 => 3 => 4

 */
