package LinkedLists;

public class Inserting_Node_Pos {
	
	class Node{
		int data;
		Node next;
		
		public Node(int data) {
			this.data=data;
			this.next=null;
		}
	}
	public Node head=null;
	public Node tail=null;
	
	//adding new node at desired location
	public void addnode(int data,int pos) {
		Node newNode=new Node(data);
		
		if(pos<0) {
			System.out.println("Invalid position ");
			return;
		}
		if(pos ==0) {
			newNode.next=head;
			head=newNode;
			if(tail==null) {
				tail=newNode;  //update tail if list was empty
			}
			return;
		}
		Node current=head;
		int currpos=0;
		while(currpos<pos-1 && current!=null) {
			current=current.next;
			currpos++;
		}
		if(current == null) {
			System.out.println("Position out of bounds for position "+pos);
			return;
		}
		newNode.next=current.next;
		current.next=newNode;
		
		if(current == tail) {
			tail=newNode;
		}
		
		}
	public void display() {
		if(head==null) {
			System.out.println("List is empty ");
			return;
		}
		Node current=head;
		System.out.print("Nodes of linkedlist: ");
		while(current!=null) {
			System.out.print(current.data);
			if(current.next!=null) {
				System.out.print("=>");
			}
			current=current.next;
		}
		System.out.println();
	}

	public static void main(String[] args) {
		Inserting_Node_Pos l=new Inserting_Node_Pos();
		l.addnode(2,0); //(data,pos)
		l.addnode(3, 1);
		l.addnode(3, 3);
		l.display();
		
	

	}

}

/*
Output:-

Position out of bounds for position 3
Nodes of linkedlist: 2=>3


 */
