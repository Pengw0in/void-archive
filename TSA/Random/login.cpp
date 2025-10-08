#include <iostream>
#include <algorithm>


int main (){
    std::string user_names[] = {"Admin", "usr1", "usr2", "usr3", "support"};
    std::string pass_words[] = {"root123", "whyme", "superpass", "pass123", "zxy@147"};

    std::string usrname;
    std::cout << "Username: ";
    std::cin >> usrname;

    std::string pass;
    std::cout << "Password: ";
    std::cin >> pass;

    auto x = std::find(user_names, user_names + 5, usrname); // std::find(arr, arr+ n, val), return a pointer pointing to that val
    int idx = x - user_names; // to get index, subtract val position with initial position
     
    if (pass_words[idx] != pass){
        std::cout << "Access denied!" << "\n";
    }
    else{
        std::cout << "Access granted!" << "\n";
    }
}