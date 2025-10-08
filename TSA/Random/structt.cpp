#include <iostream>

int main(){
   int arr[] = {1,2,34,5};
   std::cout << *(arr + 1);
   //arr is equivalent to 
   void* x = &arr;

}