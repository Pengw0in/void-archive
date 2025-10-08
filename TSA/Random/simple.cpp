#include <iostream>
// References in C++ are nothing but the alternative to 
// the already existing variable.


int main(){
    int x = 10;
    int ptr = &x;
    std::cout << ptr;
}