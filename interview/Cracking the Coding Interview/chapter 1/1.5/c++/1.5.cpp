// Example program
#include <iostream>
#include <string>
using namespace std;

string compress(string S){
    string compressed_S = "";
    int count;
    
    for (int i = 0; i < S.length(); ){
        compressed_S += S[i];
        count = 1;
        while (S[++i] == S[i-1])
            count++;
        compressed_S += '0' + count;
    }
    
    if (S.length() < compressed_S.length())
        return S;
    else
        return compressed_S;
}

int main()
{
    cout << "aaaa" << " " << compress("aaaa") << endl;
    cout << "abcd" << " " << compress("abcd") << endl;
    cout << "aaabbb" << " " << compress("aaabbb") << endl;
    cout << "aabcccccaaa" << " " << compress("aabcccccaaa") << endl;
}
