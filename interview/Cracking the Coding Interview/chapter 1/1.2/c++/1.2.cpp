#include <cstring>
#include <iostream>

using namespace std;

void reverse(char* str) {
	int n = strlen(str);
	char temp;
	for (int i=0; i<n/2; i++) {
		temp = str[i];
		str[i] = str[n-1-i];
		str[n-1-i] = temp;
	}
}

int main() {
	char str[] = "asdfqwer";
	cout << "str = " << str << "\n";
	reverse(str);
	cout << "reversed str = " << str << "\n";

	return 0;
}