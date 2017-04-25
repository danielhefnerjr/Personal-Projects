// Example program
#include <iostream>
#include <string>

using namespace std;

bool isRotation(string s1, string s2){
    if (s1.length() != s2.length()) return false;
    
    int i=0,j=0;
    
    while (s1[0] != s2[j]) { j++; }
    
    while (i < s1.length() && s1[i++] == s2[j++ % s2.length()]) {}
    
    return (i == s1.length());
}

int main()
{
    cout << isRotation("waterbottle", "erbottlewat") << endl;
    cout << isRotation("asdf", "asdf") << endl;
    cout << isRotation("asdf", "adfs") << endl;
}
