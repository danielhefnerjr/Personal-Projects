#include <iostream>

using namespace std;

template <typename T>
class Node {
	public:
	Node () { this->next = 0; }
	Node (T data, Node<T>* next) {
		this->data = data;
		this->next = next;
	}
	
	T data;
	Node<T> * next;
};

template <typename T>
class LinkedList {
	public:
	LinkedList() { this->head = 0;}
	LinkedList(Node<T>* head) { this->head  = head;}
	
	void insert(T data) {
		Node<T>* n = new Node<T>(data, head);
		head = n;
	}
	
	Node<T>* search(T data) {
		Node<T> * curr = head;
		
		while (curr && curr->data != data) {
			curr = curr->next;
		}
		
		return curr;
	}
	
	bool isPalindrome() {
		LinkedList<T> reverseList = LinkedList<T>();
		Node<T>* curr = head;
		while (curr) {
			reverseList.insert(curr->data);
			curr = curr->next;
		}
		
		Node<T>* curr1 = head;
		Node<T>* curr2 = reverseList.head;
		while (curr1 && curr2)
		{
			if (curr1->data != curr2->data)
				return false;
			
			curr1 = curr1->next;
			curr2 = curr2->next;
		}
		
		return true;
	}
	
	void print() {
		Node<T>* curr = head;
		while (curr){
			cout << curr->data << " ";
			curr = curr->next;
		}
		cout << endl;
	}
	Node<T>* head;
	
	
};


int main() {
	LinkedList<char> L = LinkedList<char>();
	
	L.insert('r');
	L.insert('a');
	L.insert('c');
	L.insert('e');
	L.insert('c');
	L.insert('a');
	L.insert('r');
	L.print();
	cout << L.isPalindrome() << endl;
	
	
	L = LinkedList<char>();
	
	L.insert('r');
	L.insert('a');
	L.insert('c');
	L.insert('e');
	L.insert('c');
	L.insert('a');
	L.print();
	cout << L.isPalindrome();
	return 0;
}