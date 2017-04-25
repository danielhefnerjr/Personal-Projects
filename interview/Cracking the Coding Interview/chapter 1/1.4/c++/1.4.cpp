#include <iostream>
#include <cstring>

using namespace std;

void repl_space_memmove(char *S){
	for (int i=0; i< strlen(S); i++){
		if (S[i] == ' '){
			memmove(S+i+3,S+i+1,strlen(S) - i + 1);
			S[i] = '%';
			S[i+1] = '2';
			S[i+2] = '0';
			i+=1;
			//cout << S<< " " << strlen(S) <<endl;
		}
	}
}

int main() {
	char a[] = "asdf asdf ";
	int num_spaces = 2;
	char * S;
	S = (char*) malloc(sizeof(a) + num_spaces*2);
	memcpy(S,a,sizeof(a));
	
	cout << S << endl;
	repl_space_memcpy(S);
	cout << S << endl;
	
	return 0;
}