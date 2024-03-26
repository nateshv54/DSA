package LinkedLists;

import LinkedLists.LinkedList.Node;

public class SLL_del_LastNode {
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
	public void addnewnode(int data) {
		Node newnode=new Node(data);
		if(head==null) {
			head=newnode;
			tail=newnode;
		}
		else {
			tail.next=newnode;
			tail=newnode;
		}
		
	}
	public void addnodepos(int data,int pos) {
		Node newnode=new Node(data);
		if(pos<0) {
			System.out.print("Invalid position");
		}
		if(pos==0) {
			newnode.next=head;
			head=newnode;
			if(tail==null) {
				tail=newnode;
			}
			return;
		}
		Node current=head;
		int currpos=0;
		//iterate the pointer upto last but one given position
		//and check if there is any empty nodes on the way
		
		
		while(currpos<pos-1 && current!=null) {
			current=current.next;
			currpos++;
		}
		
		//if there are empty nodes, raise exception
		if(current==null) {
			System.out.print("Out of bounds for postions "+pos);
			return;
		}
		
		//Set newnode address to current node address
		newnode.next=current.next;
		
		//Set address of current node to newnode address
		current.next=newnode;
		
		if(current==tail) {
			tail=newnode;
		}
	}
	public void del_lastnode() {
		if(head==null && tail==null) {
			System.out.print("List is empty");		
			}
		if(head==tail) {
			head=tail=null;
			return;
		}
		Node current=head;
		
		//set the pointer to 2nd last node
		
		while(current.next!=tail) {         
			current=current.next;      
		}
		
		//deleting last node
		
		current.next=null;
		
		//setting tail to 2nd last node
		
		tail=current;
	}


	public void display() {
		if(head==null) {
			System.out.println("List is empty");
			return;
		}
		System.out.println("Node of Linkedlist : ");
		Node current=head;
		while(current!=null) {
			System.out.print(current.data);
			if(current.next!=null) {
				System.out.print(" => ");
			}
			current=current.next;
		}
		System.out.println();
	}
	 static public void  main(String args[]) {
		 SLL_del_LastNode l=new SLL_del_LastNode();
		 l.addnewnode(14);
		 l.addnewnode(11);
		 l.display();
		 l.addnodepos(2, 0);
		 l.addnodepos(4, 1);
		 l.addnodepos(6, 2);
		 l.addnodepos(7, 3);
		 l.display();
		 l.del_lastnode();
		 l.display();
	}

}
