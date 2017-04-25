// Example program
#include <iostream>
#include <string>
using namespace std;
bool isPermutation(string S1, string S2){
    if (S1.length() != S2.length()) return false;
    
    bool found = false;
    
    for (int i = 0; i < S1.length(); i++) {
        found = false;
        for (int j = 0; j < S2.length(); j++) {
            if (S1[i] == S2[j]){
                if (found) 
                    return false;   
                else
                    found = true;
            }
        }
        
        if (!found)
            return false;
    }
    
    return true;    
}

int main()
{
    cout << isPermutation("asdf","asdf") << endl;
    cout << isPermutation("asdf","fdsa") << endl;
    cout << isPermutation("asdf","aadf") << endl;
    cout << isPermutation("qwer","ewqr") << endl;
	
	return 0;
}
