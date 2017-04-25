#include <iostream>

using namespace std;

template <typename T>
class Node {
	public:
	Node(){}
	Node(T data) { 
		this->data = data; 
		this->next = 0;
	}
	
	Node(T data, Node<T>* next){
		this->data = data;
		this->next = next;
	}
	
	T data;
	Node<T>* next;
};


template <typename T>
class LinkedList {
	public:
	LinkedList() { this->head = 0;}
	LinkedList(Node<T>* head) { this->head = head;}
	void insert(T data){
		Node<T> * n = new Node<T>(data,head);
		head = n;
	}
	
	Node<T>* search(T data){
		Node<T>* curr = head;
		
		while (curr && curr->data != data){
			curr = curr->next;
		}
		
		return curr;
	}
	
	void print(){
		Node<T>* curr = head;
		while (curr){
			cout << curr->data << " ";
			curr = curr->next;
		}
		
		cout << endl;
	}
	
	Node<T>* head;
	
};


LinkedList<int> add(LinkedList<int> list1, LinkedList<int> list2){
	LinkedList<int> sum = LinkedList<int>();
	
	int n1, n2;
	Node<int>* N1, * N2;
	
	N1 = list1.head;
	N2 = list2.head;
	
	int carry = 0;
	int s;
	while (N1 && N2){
		n1 = N1->data;
		n2 = N2->data;
		s = n1 + n2 + carry;
		carry = s / 10;
		s = s % 10;
		sum.insert(s);
		
		N1 = N1->next;
		N2 = N2->next;
	}
	
	while (N1){
		n1 = N1->data;
		s = n1 + carry;
		carry = s / 10;
		s = s % 10;
		sum.insert(s);
		
		N1 = N1->next;
	}
	
	while (N2) {
		n2 = N2->data;
		s = n2 + carry;
		carry = s / 10;
		s = s % 10;
		sum.insert(s);
		
		N2 = N2->next;
	}
	
	return sum;
}

LinkedList<int> add_reverse(LinkedList<int> list1, LinkedList<int> list2){
	
}

int main(){
	LinkedList<int> l1 = LinkedList<int>(new Node<int>(7, new Node<int>(1, new Node<int>(6)))),
					l2 = LinkedList<int>(new Node<int>(5, new Node<int>(9, new Node<int>(2))));
	l1.print();
	l2.print();
	add(l1,l2).print();
	
	return 0;
}