package LinkedLists;

import java.util.Scanner;

public class Linkedlist_creation {

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
	
	//adding new node to list
	public void addNode(int data) {
		Node newNode=new Node(data);
		
		if(head==null) {
			head=newNode;
			tail=newNode;
		}
		else {
			tail.next=newNode;
			tail=newNode;
		}
	}
	
	public void display() {
		if(head==null) {
			System.out.println("List is empty");
			return;
			}
		Node current=head;
		System.out.println("Nodes of the linkedlist");
		while(current!= null) {
			System.out.print(current.data);
			if(current.next!=null) {
				System.out.print("=>");
			}
			current=current.next;
		}
		System.out.println();
		
	}
	public static void main(String[] args) {
		Linkedlist_creation l=new Linkedlist_creation();
		l.addNode(10);
		l.addNode(11);
		l.addNode(12);
		
		//displaying linkedlist
		l.display();
	}


}
