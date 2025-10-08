#include <iostream>

void sort_array(int arr[],int sort_number){
    
}

int main(){
    int n, sort_number;

    //Prompting user about number of elements
    std::cout << "How many elements do you want to sort?" << std::endl << "Enter a Number: ";
    std::cin  >> n;
    int num[n];

    //Promting user for elements
    std::cout << "Enter Elements [Ex: 1 3 5 4 2]: ";

    //loop to push elements into the array
    for (int i= 0; i< n; i++){
        std::cin >> num[i];
    }

    for(const auto& elements : num){
        std::cout << elements << " " ;
    }

    sort_array(num,sort_number);
        
}
