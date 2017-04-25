#include <iostream>

using namespace std;

template <typename T>
class Node {
	public:
	Node() { }
	
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
	LinkedList () { this->head = 0;}
	void insert(T data){
		Node<T> * n = new Node<T>(data,head);
		head = n;
	}
	
	Node<T>* search(T data) {
		Node<T>* curr = head;
		while (curr && curr->data != data){
			curr = curr->next;
		}
		
		return curr;
	}
	void partition(T x){
		Node<T>* node_x = search(x);
		Node<T>* prev;
		Node<T>* curr = head;
		
		bool past_x = false;
		while (curr){
			if (curr == node_x) {
				past_x = true;
				prev = curr;
				curr = curr->next;
			}
			else {
				if (!past_x && curr->data > node_x->data){
					//move to X
					Node<T>* next = curr->next;
					if (curr == head)
						head = head->next;
					else
						prev->next = next;
					curr->next = node_x->next;
					node_x->next = curr;
					curr = next;
				}
				else if (past_x && curr->data < node_x->data){
					// move to head
					Node<T>* next = curr->next;
					curr->next = head;
					head = curr;
					prev->next = next;
					curr = next;
				}
				else {
					prev = curr;
					curr = curr->next;
				}
			}
				
		}
	}
	
	void print(){
		Node<T>* curr = head;
		while (curr){
			cout << curr->data << " ";
			curr = curr->next;
		}
		cout << endl;
	}
	private:
	Node<T>* head;
};


int main(){
	LinkedList<int> L = LinkedList<int>();
	
	cout << "3 middle of list:\n";
	L.insert(4);
	L.insert(2);
	L.insert(3);
	L.insert(1);
	L.insert(5);
	L.print();
	L.partition(3);
	L.print();
	
	L = LinkedList<int>();
	cout << "3 head of list:\n";
	L.insert(4);
	L.insert(2);
	L.insert(1);
	L.insert(5);
	L.insert(3);
	L.print();
	L.partition(3);
	L.print();
	
	L = LinkedList<int>();
	cout << "3 end of list:\n";
	L.insert(3);
	L.insert(4);
	L.insert(2);
	L.insert(1);
	L.insert(5);
	L.print();
	L.partition(3);
	L.print();
	return 0;
}