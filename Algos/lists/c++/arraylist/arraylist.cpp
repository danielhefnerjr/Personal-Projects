#include 
template <class T>

const int default_length = 10;

class ArrayList{
		ArrayList(){
			size = 0;
			max_length = default_length;
			data = new T[default_length];
		}
		
		ArrayList(int l){
			size = 0;
			max_length = l;
			data = new T[l];
		}
	
		int insert(T x){
			if (size == max_length) {
				resize(max_length*2);
			}
			
			data[++size] = x;
		
			return size;
		}
		
		int insertAt(T x, int n){
			// n: 0-based index
			if (size + 1 == max_length) {
				resize(max_length*2);
			}
			
			//shift everything right
			for (int i = size-1; i > n; i++) {
				data[i] = data[i-1]
			}
			
			data[n] = x;
			size++;
		}
		
		void remove(T x) {
			
		
		}
		
		void removeAt(int n){
			// shift left
			for (int i = n; i < size-1; i++) {
				data[i] = data[i+1]
			}
			size--;
		}
	private:
		void resize(int n){
			T* temp = new T[n];
			memcpy( temp, data, size * sizeof(int) );
			size = n;
			delete [] data;
			data = temp;
		}
	
		T* data;
		int size;
		int max_length;
}