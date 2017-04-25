// Example program
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

template <typename T>
class Node {
public:
    Node() {}
    Node(T dat, Node<T> *nex = 0){
        data = dat;
        next = nex;
    }
    
    T data;
    Node<T> *next;
};

template <typename T>
class LinkedList {
public:
    LinkedList() { head = 0; }
    
    LinkedList(Node<T> *h) {
        head = h;
    }
    
    void insert(T data){
        Node<T>* n = new Node<T>(data,head);
        head = n;
    }
    
    Node<T>* search(T data){
        Node<T>* curr = this.head;
        while (curr && curr->data != data) {
            curr = curr->next;
        }
    }
    
    void remove(T data) {
        Node<T>* prev;
        Node<T>* curr = this.head;   
        while (curr && curr->data != data) {
            prev = curr;
            curr = curr->next;
        }
        
        if (curr) {
            if (prev) {
                prev->next = curr->next;   
            }
            else {
                head = curr->next;
            }
            
            delete curr;
        }
    }
    
    void removeDupes(){
        vector<T> seen;
        
        Node<T> * prev;
        Node<T> * curr = head;
        while (curr) {
            if (find(seen.begin(),seen.end(),curr->data) != seen.end()) {
                // dupe (remove)
				Node<T> * next = curr->next;
				delete curr;
                prev->next = next;
                curr = next;
            }
            else {
                seen.push_back(curr->data); 
				prev = curr;
                curr = curr->next;
            }
        }
    }
	
	void removeDupes_noBuffer() {
		Node<T> * prev1;
		Node<T> * curr1 = head;
		
		while (curr1) {
			Node<T> * prev2 = curr1;
			Node<T> * curr2 = curr2;
			while (curr2) {
				if (curr2->data == curr1->data) {
					//remove
					Node<T>* next = curr2->next;
					prev2->next = next;
					delete curr2;
					curr2 = next;
				}
				else {
					prev2 = curr2;
					curr2 = curr2->next;
				}
			}
			prev1 = curr1;
			curr1 = curr1->next;
		}
	}
    
    void print() {
        Node<T> * curr = head;
        while (curr){
            cout << curr->data << " ";
            curr = curr->next;
        }
        
        cout << endl;
    }
    
private:
    Node<T> *head;
};

int main()
{
    //cout << "a";
	cout << "Remove Dupes\n";
  LinkedList<int> L = LinkedList<int>();
  L.insert(1);
  L.insert(2);
 L.insert(3);
  L.insert(2);
  L.print();
  cout << endl;
  L.removeDupes();
  L.print();
  
  cout << "Remove Dupes no buffer\n";
  L = LinkedList<int>();
  L.insert(1);
  L.insert(2);
 L.insert(3);
  L.insert(2);
  L.print();
  cout << endl;
  L.removeDupes_noBuffer();
  L.print();
}
