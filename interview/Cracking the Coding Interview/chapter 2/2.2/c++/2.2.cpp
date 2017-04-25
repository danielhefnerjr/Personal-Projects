// Example program
#include <iostream>
#include <string>

using namespace std;
template <typename T>
class Node{
public:
    Node() {}
    Node(T dat, Node<T>* nex) {
        data = dat;
        next = nex;
    }
    
    T data;
    Node<T>* next;
};

template <typename T>
class LinkedList {
public:
    LinkedList() {}
    LinkedList(Node<T>* head) {
        head = head;   
    }
    
    void insert(T data) {
        Node<T>* n = new Node<T>(data,head);   
        head = n;
    }
    
    Node<T>* search(T data) {
        Node<T>* curr = head;
        while (curr && curr->data != data){
            curr = curr->next;    
        }
        
        return curr;
    }
    
    void remove(T data) {
        Node<T>* prev;
        Node<T>* curr = head;
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
    
    Node<T>* findKthToLast(int k){
        // find length
        int len = 0;
        Node<T>* curr = head;
        while (curr) {
            len++;
            curr = curr->next;
        }
        
		curr = head;
		
        for (int i = 0; i < len-k; i++, curr = curr->next);
        
        return curr;
    }
    
    
private:
    Node<T>* head;
};

int main()
{
  LinkedList<int> L = LinkedList<int>();
  L.insert(1);
  L.insert(2);
  L.insert(3);
  L.insert(4);
  cout << L.findKthToLast(3)->data << endl; // 3
  cout << L.findKthToLast(2)->data << endl; // 2
  
  return 0;
}
