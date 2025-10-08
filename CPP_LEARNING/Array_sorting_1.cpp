#include <iostream>

int main(){
    int count;
    std::cout << "Number Elements you want to sort: ";
    std::cin >> count;
    int numbers[count];
    int n = count;
    int sort_number = (n * (n - 1))/2;
    int cng;
    bool swapped;
    

    //for pushing user inputs into array
    for(int i = 0; i <count; i++){
        int input;
        std::cout << "Input your number: ";
        std::cin >> input;
        numbers[i] = input;  
    }

    while(sort_number > 0){
        swapped = false;
        cng = 0;
        
        while(cng < (count - 1)){
            if(numbers[cng] > numbers[cng + 1]){
            numbers[cng] = numbers[cng] + numbers[cng + 1];
            numbers[cng + 1] = numbers[cng] - numbers[cng + 1];
            numbers[cng] = numbers[cng] - numbers[cng + 1];

            swapped = true;
        }
        cng++;
      }
        if(!swapped){
            break;
        }
      sort_number--;
    }

    for(const auto& elements : numbers){
        std::cout << elements << " " ;
    }
    
}
